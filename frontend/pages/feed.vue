<template>
  <div>
    <title-bar :title-stack="titleStack" />
    <hero-bar>
      Gerenciamento de Rações
      <template v-slot:right>
        <router-link to="/" class="button"> Dashboard </router-link>
      </template>
    </hero-bar>
    <section class="section is-main-section">
      <card-component
        title="Rações"
        icon="silverware"
        class="has-table has-mobile-sort-spaced"
      >
        <list-feed />
      </card-component>
    </section>
  </div>
</template>

<script>
import ListFeed from '../components/feeds/ListFeed.vue'
import CardComponent from '../components/templates/CardComponent.vue'
import HeroBar from '@/components/templates/HeroBar'
import TitleBar from '../components/templates/TitleBar.vue'
export default {
  components: { TitleBar, HeroBar, CardComponent, ListFeed },
  data() {
    return {}
  },
  computed: {
    titleStack() {
      return ['Admin', 'Rações']
    }
  }
}
</script>

<style></style>
