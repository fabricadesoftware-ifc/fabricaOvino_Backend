<template>
  <div>
    <title-bar :title-stack="titleStack" />
    <hero-bar>
      Gerenciamento de rações
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
import TitleBar from '@/components/templates/TitleBar'
import HeroBar from '@/components/templates/HeroBar'
import CardComponent from '@/components/templates/CardComponent'

import ListFeed from '@/components/feeds/ListFeed'
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
