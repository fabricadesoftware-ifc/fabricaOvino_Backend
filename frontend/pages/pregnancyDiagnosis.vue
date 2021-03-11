<template>
  <div class="pregnancy-diagnosis">
    <title-bar :title-stack="titleStack" />
    <hero-bar>
      {{ $t('pages.admin.breed.title') }}
      <template v-slot:right>
        <router-link to="/" class="button"> Dashboard </router-link>
      </template>
    </hero-bar>
    <section class="section is-main-section">
      <card-component title="Novo diagnóstico" icon="ballot">
        <form-pregnancy-diagnosis />
      </card-component>
    </section>
  </div>
</template>

<script>
import TitleBar from '@/components/templates/TitleBar'
import HeroBar from '@/components/templates/HeroBar'
import CardComponent from '@/components/templates/CardComponent'
import FormPregnancyDiagnosis from '@/components/sheeps/FormPregnancyDiagnosis'

export default {
  components: { FormPregnancyDiagnosis, TitleBar, HeroBar, CardComponent },
  computed: {
    titleStack() {
      return ['Admin', 'Ovelhas', this.$t('pages.admin.breed.title')]
    }
  }
}
</script>

<style></style>
