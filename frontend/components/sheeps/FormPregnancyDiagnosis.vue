<template>
  <form @submit.prevent="save">
    <b-field
      :label="$t('pages.admin.pregnancyDiagnosis.forms.sheep.label')"
      horizontal
    >
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

    <v-datetime
      v-model="date"
      :label="$t('pages.admin.pregnancyDiagnosis.forms.dateTime.label')"
    />

    <b-field label="Diagnóstico" horizontal>
      <b-switch
        v-model="pregnancyDiagnosis.diagnosis"
        :true-value="true"
        :false-value="false"
      >
        <strong>{{
          $t('pages.admin.pregnancyDiagnosis.forms.pregnancyDiagnosis')
        }}</strong>
      </b-switch>
    </b-field>
    <b-field horizontal>
      <b-field grouped>
        <div class="control">
          <b-button native-type="submit" type="is-primary">{{
            $t('buttons.save')
          }}</b-button>
        </div>
        <div class="control">
          <b-button
            type="is-primary is-outlined"
            @click.prevent="$parent.close()"
            >{{ $t('buttons.reset') }}</b-button
          >
        </div>
      </b-field>
    </b-field>
  </form>
</template>

<script>
import { mapState, mapGetters, mapActions } from 'vuex'
import VDatetime from '@/components/templates/VDatetime'
export default {
  components: { VDatetime },
  data() {
    return {
      date: new Date(),
      pregnancyDiagnosis: {
        diagnosis: false
      }
    }
  },
  computed: {
    ...mapState('auth', ['user']),
    ...mapGetters('sheeps', ['notPregnantSheeps'])
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
