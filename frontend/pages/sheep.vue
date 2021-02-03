<template>
  <div class="sheep-admin">
    <title-bar :title-stack="titleStack" />

    <hero-bar>
      {{ $t('pages.admin.sheep.title') }}
      <template v-slot:right>
        <div class="buttons">
          <button class="button is-primary" @click="addNewSheep = true">
            {{ $t('pages.sheeps.add') }}
          </button>
          <router-link to="/" class="button"> Dashboard </router-link>
        </div>
      </template>
    </hero-bar>

    <b-modal
      :active.sync="addNewSheep"
      has-modal-card
      trap-focus
      :destroy-on-hide="false"
      aria-role="dialog"
      aria-modal
    >
      <form-add-sheep />
    </b-modal>

    <hr />
    <card-component
      class="has-table has-mobile-sort-spaced"
      title="Animais"
      icon="sheep"
    >
      <list-sheep />
    </card-component>
  </div>
</template>

<script>
import FormAddSheep from '@/components/sheeps/FormAddSheep'
import ListSheep from '@/components/sheeps/ListSheep'
import TitleBar from '@/components/templates/TitleBar'
import HeroBar from '@/components/templates/HeroBar'
import CardComponent from '@/components/templates/CardComponent'

export default {
  components: { FormAddSheep, ListSheep, TitleBar, HeroBar, CardComponent },
  data() {
    return {
      addNewSheep: false
    }
  },
  computed: {
    titleStack() {
      return ['Admin', this.$t('pages.admin.sheep.title')]
    }
  }
}
</script>
