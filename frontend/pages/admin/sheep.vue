<template>
  <div class="sheep-admin">
    <PageTitle
      icon="sheep"
      :main="$t('pages.admin.sheep.title')"
      :sub="$t('pages.admin.sheep.subtitle')"
    />

    <button class="button is-primary is-medium" @click="addNewSheep = true">
      Adicionar novo animal
    </button>

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
    <list-sheep v-model="sheeps" />
  </div>
</template>

<script>
import { mapState } from 'vuex'

import FormAddSheep from '@/components/sheeps/FormAddSheep'
import ListSheep from '@/components/sheeps/ListSheep'
import PageTitle from '@/components/templates/PageTitle'

import { showError } from '@/plugins/global'
export default {
  components: { FormAddSheep, ListSheep, PageTitle },
  data: function () {
    return {
      addNewSheep: false
    }
  },
  computed: {
    ...mapState('sheeps', ['sheeps'])
  }
}
</script>

<style></style>
