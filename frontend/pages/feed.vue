<template>
  <div>
    <title-bar :title-stack="titleStack" />
    <hero-bar>
<<<<<<< HEAD
      Gerenciamento de rações
=======
      Gerenciamento de Rações
>>>>>>> origin/Dev-Maria
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
<<<<<<< HEAD
import TitleBar from '@/components/templates/TitleBar'
import HeroBar from '@/components/templates/HeroBar'
import CardComponent from '@/components/templates/CardComponent'

import ListFeed from '@/components/feeds/ListFeed'
=======
import ListFeed from '../components/feeds/ListFeed.vue'
import CardComponent from '../components/templates/CardComponent.vue'
import HeroBar from '@/components/templates/HeroBar'
import TitleBar from '../components/templates/TitleBar.vue'
>>>>>>> origin/Dev-Maria
export default {
  components: { TitleBar, HeroBar, CardComponent, ListFeed },
  data() {
    return {}
  },
<<<<<<< HEAD

=======
>>>>>>> origin/Dev-Maria
  computed: {
    titleStack() {
      return ['Admin', 'Rações']
    }
  }
}
</script>

<style></style>
