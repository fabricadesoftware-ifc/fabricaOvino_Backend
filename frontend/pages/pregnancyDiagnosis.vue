<template>
  <div class="pregnancy-diagnosis">
    <PageTitle
      icon="medical-bag"
      :main="$t('pages.admin.pregnancyDiagnosis.title')"
      :sub="$t('pages.admin.pregnancyDiagnosis.subtitle')"
    />

    <form-pregnancy-diagnosis />
  </div>
</template>

<script>
import PageTitle from '@/components/templates/PageTitle'
import FormPregnancyDiagnosis from '@/components/sheeps/FormPregnancyDiagnosis'
// import { mapState, mapActions, mapGetters } from 'vuex'
export default {
  components: { FormPregnancyDiagnosis, PageTitle }
  // data() {
  //   return {
  //     date: new Date(),
  //     pregnancyDiagnosis: {
  //       diagnosis: false
  //     }
  //   }
  // },
  // computed: {
  //   ...mapState('auth', ['user']),
  //   ...mapGetters('sheeps', ['notPregnantSheeps'])
  // },
  // methods: {
  //   ...mapActions('sheeps', ['getSheeps']),
  //   reset() {
  //     this.pregnancyDiagnosis = {
  //       diagnosis: false
  //     }
  //   },
  //   async save() {
  //     this.pregnancyDiagnosis.date = this.date.toISOString()
  //     this.pregnancyDiagnosis.user = this.user.id
  //     try {
  //       await this.$axios.$post(
  //         '/api/v1/pregnancy-diagnosis/',
  //         this.pregnancyDiagnosis
  //       )
  //       this.$toasted.global.defaultSuccess()
  //       this.getSheeps()
  //       this.reset()
  //     } catch (err) {
  //       for (const item in err.response.data) {
  //         this.$toast.error(item + ': ' + err.response.data[item])
  //       }
  //     }
  //   }
  // }
}
</script>

<style></style>
