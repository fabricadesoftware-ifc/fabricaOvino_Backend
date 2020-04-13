<template>
  <div class="category-admin">
    <PageTitle
      icon="alpha-c-circle-outline"
      :main="$t('pages.admin.category.title')"
      :sub="$t('pages.admin.category.subtitle')"
    />
    <div class="form">
      <input type="hidden" id="category-id" v-model="category.id" />
      <b-field :label="$t('pages.admin.forms.name.label')" class="category-form-fields">
        <b-input
          :placeholder="$t('pages.admin.forms.name.placeholder')"
          type="text"
          icon="tag"
          v-model="category.name"
          :readonly="mode === 'remove'"
          required
        />
      </b-field>
      <div class="category-form-buttons">
        <b-button v-if="mode === 'save'" type="is-info" icon-left="check" @click="save">
          {{ $t("buttons.save") }}
        </b-button>
        <b-button v-else type="is-danger" icon-left="trash-can-outline" @click="remove">
          {{ $t("buttons.delete") }}
        </b-button>
        <b-button type="is-dark" icon-left="redo" @click="reset">
          {{ $t("buttons.reset") }}
        </b-button>
      </div>
    </div>
    <hr />
    <b-table striped :data="categories">
      <template slot-scope="props">
        <b-table-column
          v-for="(column, index) in columns"
          :key="index"
          :field="column.field"
          :sortable="column.sortable"
          :label="column.label"
        >
          {{ props.row[column.field] }}
        </b-table-column>

        <b-table-column field="actions" :label="$t('pages.admin.category.table.actions')">
          <b-button type="is-warning" icon-left="pencil" @click="loadCategory(props.row)"> </b-button>
          <b-button type="is-danger" icon-left="trash-can-outline" @click="loadCategory(props.row, 'remove')">
          </b-button>
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
      category: {},
      categories: [],
      columns: [
        { field: "id", label: this.$t("pages.admin.category.table.id"), sortable: true },
        { field: "name", label: this.$t("pages.admin.category.table.name"), sortable: true },
      ],
    };
  },
  async fetch() {
    this.categories = await this.$axios.$get("/api/v1/categories/");
  },
  methods: {
    loadCategory(category, mode = "save") {
      this.mode = mode;
      this.category = {
        id: category.id,
        name: category.name,
      };
    },
    reset() {
      this.category = {};
      this.mode = "save";
      this.$fetch();
    },
    save() {
      const method = this.category.id ? "put" : "post";
      const id = this.category.id ? `/${this.category.id}` : "";
      const url = `/api/v1/categories${id}/`;
      this.$axios[method](url, this.category)
        .then(() => {
          this.$toasted.global.defaultSuccess();
          this.reset();
        })
        .catch(showError);
    },
    remove() {
      const id = this.category.id;
      const url = `/api/v1/categories/${id}`;
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
