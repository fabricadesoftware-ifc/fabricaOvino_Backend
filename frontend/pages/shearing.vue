<template>
  <div class="shearing">
    <title-bar :title-stack="titleStack" />
    <hero-bar>
      {{ $t('pages.admin.breed.title') }}
      <template v-slot:right>
        <router-link to="/" class="button"> Dashboard </router-link>
      </template>
    </hero-bar>
    <section class="section is-main-section">
      <card-component title="Nova Tosquia" icon="ballot">
        <form-shear />
      </card-component>
    </section>
  </div>
</template>
<script>
import CardComponent from '../components/templates/CardComponent.vue'
import HeroBar from '@/components/templates/HeroBar'
import TitleBar from '../components/templates/TitleBar.vue'
import FormShear from '../components/sheeps/FormShear.vue'
export default {
  components: { FormShear, TitleBar, HeroBar, CardComponent },
  computed: {
    titleStack() {
      return ['Admin', 'Ovelhas', this.$t('pages.admin.shearing.title')]
    }
  }
}
</script>

<style></style>
