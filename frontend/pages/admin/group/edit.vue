<template>
  <div class="group-edit">
    <PageTitle
      icon="face"
      :main="$t('pages.admin.group.edit.title')"
      :sub="$t('pages.admin.group.edit.subtitle')"
    />

    <general-info :group="group" edit />
    <permissions :choosedIds="choosedIds" @update-choosed="updateChoosed" edit />

    <div class="form-bottons columns is-mobile is-centered">
      <div class="column is-3">
        <b-button type="is-info" icon-left="check" @click="save">{{ $t('buttons.save') }}</b-button>
        <b-button type="is-dark" icon-left="redo" @click="reset">{{ $t('buttons.reset') }}</b-button>
      </div>
    </div>
  </div>
</template>

<script>
import PageTitle from '@/components/templates/PageTitle'
import GeneralInfo from '@/components/group/GeneralInfo'
import Permissions from '@/components/group/Permissions'

import { showError } from '@/plugins/global'
export default {
  components: { PageTitle, GeneralInfo, Permissions },
  data() {
    return {
      choosedIds: [],
      group: {},
      originalGroup: {}
    }
  },
  async fetch() {
    this.group = this.$route.params.group
    Object.assign(this.originalGroup, this.group)
    this.choosedIds= this.group.permissions.map( ({id}) => id)
  },

  methods: {
    reset() {
      Object.assign(this.group, this.originalGroup)
    },

    updateChoosed(ids) {
      this.choosedIds = ids
    },

    save() {
      const id = this.group.id
      this.group.permissions = this.choosedIds
      const url = `/api/v1/groups/${id}/`
      this.$axios
        .$put(url, this.group)
        .then(res => {
          this.$toasted.global.defaultSuccess()
          this.reset()
          sthis.group = res
        })
        .catch(showError)
    }
  }
}
</script>

<style>
</style>
