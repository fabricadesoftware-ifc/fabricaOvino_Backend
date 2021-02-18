<template>
  <div class="breed-admin">
    <title-bar :title-stack="titleStack" />
    <hero-bar>
      {{ $t('pages.admin.breed.title') }}
      <template v-slot:right>
        <router-link to="/" class="button"> Dashboard </router-link>
      </template>
    </hero-bar>
    <section class="section is-main-section">
      <card-component title="Adicionar / Editar" icon="ballot">
        <form-breed v-model="breed" />
      </card-component>
      <hr />
      <card-component
        class="has-table has-mobile-sort-spaced"
        title="Raças"
        icon="puzzle"
      >
        <list-breed @loadBreed="loadBreed" />
      </card-component>
    </section>
  </div>
</template>

<script>
import TitleBar from '@/components/templates/TitleBar'
import HeroBar from '@/components/templates/HeroBar'
import CardComponent from '@/components/templates/CardComponent'

import FormBreed from '@/components/breeds/FormBreed'
import ListBreed from '@/components/breeds/ListBreed'

export default {
  auth: false,

  components: { FormBreed, ListBreed, TitleBar, HeroBar, CardComponent },
  data: function () {
    return {
      breed: {}
    }
  },
  computed: {
    titleStack() {
      return ['Admin', this.$t('pages.admin.breed.title')]
    }
  },
  methods: {
    loadBreed(breed, mode = 'save') {
      this.mode = mode
      this.breed = {
        id: breed.id,
        name: breed.name
      }
    }
  }
}
</script>

<style></style>
