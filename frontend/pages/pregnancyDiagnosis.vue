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

export default {
  components: { FormPregnancyDiagnosis, PageTitle }
}
</script>

<style></style>
