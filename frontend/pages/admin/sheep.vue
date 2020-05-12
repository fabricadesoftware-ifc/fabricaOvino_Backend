<template>
  <div class="sheep-admin">
    <PageTitle
      icon="sheep"
      :main="$t('pages.admin.sheep.title')"
      :sub="$t('pages.admin.sheep.subtitle')"
    />
    <div class="form">
      <input type="hidden" id="sheep-id" v-model="sheep.id" />
      <b-field :label="$t('pages.admin.sheep.forms.earringNumber.label')" class="sheep-form-fields">
        <b-input
          :placeholder="$t('pages.admin.sheep.forms.earringNumber.placeholder')"
          type="text"
          icon="tag"
          v-model="sheep.earringNumber"
          :readonly="mode === 'remove'"
          required
        />
      </b-field>
      <b-field :label="$t('pages.admin.sheep.forms.breed.label')" class="sheep-form-fields">
        <b-select
          :placeholder="$t('pages.admin.sheep.forms.breed.placeholder')"
          icon="puzzle"
          v-model="sheep.breed"
          :readonly="mode === 'remove'"
          required
        >
          <option v-for="breed in breeds" :value="breed.id" :key="breed.id">{{ breed.name }}</option>
        </b-select>
      </b-field>
      <b-field :label="$t('pages.admin.sheep.forms.category.label')" class="sheep-form-fields">
        <b-select
          :placeholder="$t('pages.admin.sheep.forms.category.placeholder')"
          icon="alpha-c-circle-outline"
          v-model="sheep.category"
          :readonly="mode === 'remove'"
          required
        >
          <option
            v-for="category in categories"
            :value="category.id"
            :key="category.id"
          >{{ category.name }}</option>
        </b-select>
      </b-field>
      <b-field :label="$t('pages.admin.sheep.forms.birthday.label')" class="sheep-form-fields">
        <b-datepicker
          :placeholder="$t('pages.admin.sheep.forms.birthday.placeholder')"
          icon="calendar-today"
          v-model="birthday"
          :readonly="mode === 'remove'"
        />
      </b-field>
      <b-field :label="$t('pages.admin.sheep.forms.sex.label')" class="sheep-form-fields">
        <b-radio
          v-model="sheep.sex"
          name="form-sex"
          native-value="M"
        >{{ $t('pages.admin.sheep.forms.sex.male') }}</b-radio>
        <b-radio
          v-model="sheep.sex"
          name="form-sex"
          native-value="F"
        >{{ $t('pages.admin.sheep.forms.sex.female') }}</b-radio>
      </b-field>
      <b-field :label="$t('pages.admin.sheep.forms.teethQuantity.label')" class="sheep-form-fields">
        <b-numberinput
          rounded
          :placeholder="$t('pages.admin.sheep.forms.teethQuantity.placeholder')"
          icon="mdi-tooth"
          v-model="sheep.teethQuantity"
          :readonly="mode === 'remove'"
          required
        />
      </b-field>
      <div class="sheep-form-buttons">
        <b-button
          v-if="mode === 'save'"
          type="is-info"
          icon-left="check"
          @click="save"
        >{{ $t("buttons.save") }}</b-button>
        <b-button
          v-else
          type="is-danger"
          icon-left="trash-can-outline"
          @click="remove"
        >{{ $t("buttons.delete") }}</b-button>
        <b-button type="is-dark" icon-left="redo" @click="reset">{{ $t("buttons.reset") }}</b-button>
      </div>
    </div>
    <hr />
    <b-table striped :data="sheeps">
      <template slot-scope="props">
        <b-table-column
          v-for="(column, index) in columns"
          :key="index"
          :field="column.field"
          :sortable="column.sortable"
          :label="column.label"
        >{{ props.row[column.field] }}</b-table-column>
        <b-table-column field="pregnant" :label="$t('pages.admin.sheep.table.pregnant')">
          <span v-if="props.row.pregnant">{{$t('true')}}</span>
          <span v-else>{{$t('false')}}</span>
        </b-table-column>

        <b-table-column field="actions" :label="$t('pages.admin.sheep.table.actions')">
          <b-button type="is-warning" icon-left="pencil" @click="loadSheep(props.row)"></b-button>
          <b-button
            type="is-danger"
            icon-left="trash-can-outline"
            @click="loadSheep(props.row, 'remove')"
          ></b-button>
        </b-table-column>
      </template>
    </b-table>
  </div>
</template>

<script>
import PageTitle from "@/components/templates/PageTitle";

import { showError } from "@/plugins/global";
export default {
  components: { PageTitle },
  data: function () {
    return {
      mode: "save",
      sheep: {teethQuantity: 0},
      categories: [],
      breeds: [],
      sheeps: [],
      birthday: new Date(),
      columns: [
        { field: "id", label: this.$t("pages.admin.sheep.table.id"), sortable: true },
        { field: "earringNumber", label: this.$t("pages.admin.sheep.table.earringNumber"), sortable: true },
        { field: "breed", label: this.$t("pages.admin.sheep.table.breed"), sortable: true },
        { field: "category", label: this.$t("pages.admin.sheep.table.category"), sortable: true },
        { field: "sex", label: this.$t("pages.admin.sheep.table.sex"), sortable: true },
        { field: "birthday", label: this.$t("pages.admin.sheep.table.birthday"), sortable: true },
      ],
    };
  },
  async fetch() {
    this.categories = await this.$axios.$get("/api/v1/categories")
    this.breeds = await this.$axios.$get("/api/v1/breeds")
    this.sheeps = await this.$axios.$get("/api/v1/sheeps/");
  },
  methods: {
    loadSheep(sheep, mode = "save") {
      this.mode = mode;
      this.sheep = {
        id: sheep.id,
        earringNumber: sheep.earringNumber,
        breed: this.breeds.find( elem => elem.name == sheep.breed).id,
        category: this.categories.find( elem => elem.name == sheep.category).id,
        birthday: sheep.birthday,
        sex: sheep.sex == 'Male' ? 'M' : 'F',
        teethQuantity: sheep.teethQuantity,
        mother: sheep.mother,
        father: sheep.father
      }
    },
    reset() {
      this.sheep = {};
      this.mode = "save";
      this.$fetch();
    },
    save() {
      const method = this.sheep.id ? "put" : "post";
      const id = this.sheep.id ? `/${this.sheep.id}` : "";
      const url = `/api/v1/sheeps${id}/`;
      this.sheep.birthday = this.birthday.toLocaleDateString('fr-CA')
      console.log(this.sheep)
      this.$axios[method](url, this.sheep)
        .then(() => {
          this.$toasted.global.defaultSuccess();
          this.reset();
        })
       .catch(e => {
          for (var item in e.response.data) {
            this.$toast.error(item + ': ' + e.response.data[item])
          }
        })
    },
    remove() {
      const id = this.sheep.id;
      const url = `/api/v1/sheeps/${id}`;
      this.$axios
        .delete(url)
        .then(() => {
          this.$toasted.global.defaultSuccess();
          this.reset();
        })
        .catch(showError);
    },
  },
};
</script>

<style></style>



