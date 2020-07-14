<template>
  <div class="form">
    <b-field :label="$t('pages.admin.pregnancyDiagnosis.forms.sheep.label')">
      <b-select
        v-model="pregnancyDiagnosis.sheep"
        :placeholder="
          $t('pages.admin.pregnancyDiagnosis.forms.sheep.placeholder')
        "
        icon="sheep"
        required
      >
        <option
          v-for="sheep in notPregnantSheeps"
          :key="sheep.id"
          :value="sheep.id"
          >{{ sheep.earringNumber }}</option
        >
      </b-select>
    </b-field>
    <b-field :label="$t('pages.admin.pregnancyDiagnosis.forms.dateTime.label')">
      <select-date />
    </b-field>
    <!-- <b-field :label="$t('pages.admin.pregnancyDiagnosis.forms.dateTime.label')">
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
            <span>{{ $t('buttons.now') }}</span>
          </button>
        </template>
        <template slot="right">
          <button class="button is-danger" @click="datetime = null">
            <b-icon icon="close"></b-icon>
            <span>{{ $t('buttons.clear') }}</span>
          </button>
        </template>
      </b-datetimepicker>
    </b-field> -->
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
</template>

<script>
import { mapState, mapGetters } from 'vuex'
import { SelectDate } from '@/components/templates/SelectDate'
export default {
  components: { SelectDate },
  computed: {
    ...mapState('auth', ['user']),
    ...mapGetters('sheeps', ['notPregnantSheeps'])
  },
  data() {
    return {
      date: new Date(),
      pregnancyDiagnosis: {}
    }
  },
  methods: {
    save() {},
    reset() {}
  }
}
</script>

<style></style>
