<template>
  <div class="breed-admin">
    <PageTitle
      icon="puzzle"
      :main="$t('pages.admin.breed.title')"
      :sub="$t('pages.admin.breed.subtitle')"
    />
    <form-breed v-model="breed" />
    <hr />
    <list-breed @loadBreed="loadBreed" />
  </div>
</template>

<script>
import PageTitle from '@/components/templates/PageTitle'
import FormBreed from '@/components/breeds/FormBreed'
import ListBreed from '@/components/breeds/ListBreed'

export default {
  auth: false,
  components: { FormBreed, ListBreed, PageTitle },
  data: function () {
    return {
      breed: {}
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
