<template>
  <div class="lots">
    <title-bar :title-stack="titleStack" />
    <hero-bar>
      {{ $t('pages.lots.title') }}
      <template v-slot:right>
        <router-link to="/" class="button"> Dashboard </router-link>
      </template>
    </hero-bar>

    <section class="section is-main-section">
      <card-component title="Adicionar / Editar" icon="ballot">
        <form-lots v-model="lots" />
      </card-component>
      <hr />
      <card-component
        class="has-table has-mobile-sort-spaced"
        title="Lotes"
        icon="view-grid"
      >
        <list-lots @loadLots="loadLots" />
      </card-component>
    </section>
    {{ lots }}
  </div>
</template>

<script>
import TitleBar from '@/components/templates/TitleBar'
import HeroBar from '@/components/templates/HeroBar'
import CardComponent from '@/components/templates/CardComponent'
import FormLots from '@/components/lots/FormLots'
import ListLots from '@/components/lots/ListLots'

export default {
  components: { FormLots, ListLots, CardComponent, HeroBar, TitleBar },
  data() {
    return {
      lots: {}
    }
  },
  computed: {
    titleStack() {
      return ['Reprodução', this.$t('pages.lots.title')]
    }
  },
  methods: {
    loadLots(lots) {
      this.lots = {
        id: lots.id,
        name: lots.name,
        date: lots.date
      }
    }
  }
}
</script>
