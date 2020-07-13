<template>
  <div class="pregnancy-diagnosis">
    <PageTitle
      icon="medical-bag"
      :main="$t('pages.admin.pregnancyDiagnosis.title')"
      :sub="$t('pages.admin.pregnancyDiagnosis.subtitle')"
    />

    <div class="form">
      <input
        type="hidden"
        id="pregnancyDiagnosis-id"
        v-model="pregnancyDiagnosis.id"
      />
      <b-field
        :label="$t('pages.admin.pregnancyDiagnosis.forms.sheep.label')"
        class="pregnancyDiagnosis-form-fields"
      >
        <b-select
          :placeholder="
            $t('pages.admin.pregnancyDiagnosis.forms.sheep.placeholder')
          "
          icon="sheep"
          v-model="pregnancyDiagnosis.sheep"
          required
        >
          <option
            v-for="sheep in notPregnantSheeps"
            :value="sheep.id"
            :key="sheep.id"
            >{{ sheep.earringNumber }}</option
          >
        </b-select>
      </b-field>
      <b-field
        :label="$t('pages.admin.pregnancyDiagnosis.forms.dateTime.label')"
        class="pregnancyDiagnosis-form-fields"
      >
        <b-datetimepicker
          :placeholder="
            $t('pages.admin.pregnancyDiagnosis.forms.dateTime.placeholder')
          "
          icon="calendar-today"
          v-model="date"
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
      <b-switch
        v-model="pregnancyDiagnosis.diagnosis"
        :true-value="true"
        :false-value="false"
      >
        <strong>{{
          $t('pages.admin.pregnancyDiagnosis.forms.pregnancyDiagnosis')
        }}</strong>
      </b-switch>
      <div class="sheep-form-buttons">
        <b-button type="is-info" icon-left="check" @click="save">{{
          $t('buttons.save')
        }}</b-button>
        <b-button type="is-dark" icon-left="redo" @click="reset">{{
          $t('buttons.reset')
        }}</b-button>
      </div>
    </div>
    <hr />
  </div>
</template>

<script>
import PageTitle from '@/components/templates/PageTitle'
import { mapState, mapActions, mapGetters } from 'vuex'
export default {
  components: { PageTitle },
  computed: {
    ...mapState('auth', ['user']),
    ...mapGetters('sheeps', ['notPregnantSheeps'])
  },
  data() {
    return {
      date: new Date(),
      pregnancyDiagnosis: {
        diagnosis: false
      }
    }
  },
  methods: {
    ...mapActions('sheeps', ['getSheeps']),
    reset() {
      this.pregnancyDiagnosis = {
        diagnosis: false
      }
    },
    async save() {
      this.pregnancyDiagnosis.date = this.date.toISOString()
      this.pregnancyDiagnosis.user = this.user.id
      try {
        await this.$axios.$post(
          '/api/v1/pregnancy-diagnosis/',
          this.pregnancyDiagnosis
        )
        this.$toasted.global.defaultSuccess()
        this.getSheeps()
        this.reset()
      } catch (err) {
        for (const item in err.response.data) {
          this.$toast.error(item + ': ' + err.response.data[item])
        }
      }
    }
  }
}
</script>

<style></style>
