<template>
  <div class="group-edit">
    <PageTitle
      icon="face"
      :main="$t('pages.admin.group.add.title')"
      :sub="$t('pages.admin.group.add.subtitle')"
    />

    <general-info :group="group" edit />
    <permissions
      :choosed-ids="choosedIds"
      edit
      @update-choosed="updateChoosed"
    />

    <div class="form-bottons columns is-mobile is-centered">
      <div class="column is-3">
        <b-button type="is-info" icon-left="check" @click="save">{{
          $t('buttons.save')
        }}</b-button>
        <b-button type="is-dark" icon-left="redo" @click="reset">{{
          $t('buttons.reset')
        }}</b-button>
      </div>
    </div>
  </div>
</template>

<script>
import PageTitle from '@/components/templates/PageTitle'
import GeneralInfo from '@/components/group/GeneralInfo'
import Permissions from '@/components/group/Permissions'

export default {
  components: { PageTitle, GeneralInfo, Permissions },
  data() {
    return {
      choosedIds: [],
      group: {},
      originalGroup: {}
    }
  },

  methods: {
    reset() {
      Object.assign(this.group, this.originalGroup)
    },

    updateChoosed(ids) {
      this.choosedIds = ids
    },

    save() {
      this.group.permissions = this.choosedIds
      const url = '/api/v1/groups/'
      this.$axios
        .$post(url, this.group)
        .then(res => {
          this.$toasted.global.defaultSuccess()
          this.group = res
        })
        .catch(e => {
          for (var item in e.response.data) {
            this.$toast.error(e.response.data[item])
          }
        })
    }
  }
}
</script>

<style></style>
