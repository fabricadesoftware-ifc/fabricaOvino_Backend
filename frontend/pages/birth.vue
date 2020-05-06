<template>
  <div class="birth">
    <PageTitle
      icon="lightbulb-outline"
      :main="$t('pages.birth.title')"
      :sub="$t('pages.birth.subtitle')"
    />

    <div class="form">
      <b-tabs>
        <b-tab-item :label="$t('pages.birth.tabs.main')">
          <b-field
            :label="$t('pages.birth.forms.sheep.label')"
            class="pregnancyDiagnosis-form-fields"
          >
            <b-select
              :placeholder="$t('pages.birth.forms.sheep.placeholder')"
              icon="sheep"
              v-model="pregnancyDiagnosis.sheep"
              :readonly="mode === 'remove'"
              required
            >
              <option
                v-for="sheep in sheeps"
                :value="sheep.id"
                :key="sheep.id"
              >{{ sheep.earringNumber }}</option>
            </b-select>
          </b-field>
          <b-field
            :label="$t('pages.birth.forms.dateTime.label')"
            class="pregnancyDiagnosis-form-fields"
          >
            <b-datetimepicker
              :placeholder="$t('pages.birth.forms.dateTime.placeholder')"
              icon="calendar-today"
              v-model="date"
              :readonly="mode === 'remove'"
            >
              <template slot="left">
                <button class="button is-primary" @click="datetime = new Date()">
                  <b-icon icon="clock"></b-icon>
                  <span>Now</span>
                </button>
              </template>
              <template slot="right">
                <button class="button is-danger" @click="datetime = null">
                  <b-icon icon="close"></b-icon>
                  <span>Clear</span>
                </button>
              </template>
            </b-datetimepicker>
          </b-field>
          <b-field
            :label="$t('pages.birth.forms.newbornsQuantity.label')"
            class="birth-form-fields"
          >
            <b-numberinput
              rounded
              :placeholder="$t('pages.birth.forms.newbornsQuantity.placeholder')"
              icon="mdi-tooth"
              v-model="number"
              :readonly="mode === 'remove'"
              required
            />
          </b-field>
        </b-tab-item>

        <b-tab-item v-for="n in number" :key="n" :label="$t('pages.birth.tabs.newborn') + ' ' + n">
          <GroupAdmin />
        </b-tab-item>
      </b-tabs>
      <input type="hidden" id="birth-id" v-model="pregnancyDiagnosis.id" />

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
  </div>
</template>

<script>
import PageTitle from '@/components/templates/PageTitle'
export default {
  components: { PageTitle },
  data () {
    return {
      mode: "save",
      number: 0,
      date: new Date(),
      pregnancyDiagnosis: {},
      sheeps: [],
      users: [],
      pregnancyDiagnostics: []
    }
  },
  async fetch() {
    this.pregnancyDiagnostics = await this.$axios.$get("/api/v1/pregnancy-diagnosis")
    this.users = await this.$axios.$get("/api/v1/users")
    this.sheeps = await this.$axios.$get("/api/v1/sheeps/");
  },
  methods: {
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
        .catch(e  => {
          for (const key in e.response.data) {
            if (e.response.data.hasOwnProperty(key)) {
              const element = e.response.data[key];
              showError(element[0])
            }
          }
        });
    },
  }
}
</script>

<style>
</style>
