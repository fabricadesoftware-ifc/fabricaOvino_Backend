<template>
  <div class="sheep-admin">
    <PageTitle
      icon="sheep"
      :main="$t('pages.admin.sheep.title')"
      :sub="$t('pages.admin.sheep.subtitle')"
    />

    <button class="button is-primary is-medium" @click="addNewSheep = true">
      {{ $t('pages.sheeps.add') }}
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
    <list-sheep />
  </div>
</template>

<script>
import FormAddSheep from '@/components/sheeps/FormAddSheep'
import ListSheep from '@/components/sheeps/ListSheep'
import PageTitle from '@/components/templates/PageTitle'

export default {
  components: { FormAddSheep, ListSheep, PageTitle },
  data() {
    return {
      addNewSheep: false
    }
  }
}
</script>
