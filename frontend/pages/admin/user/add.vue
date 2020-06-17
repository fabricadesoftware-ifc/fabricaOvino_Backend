<template>
  <div class="user-edit">
    <PageTitle
      icon="face"
      :main="$t('pages.admin.user.add.title')"
      :sub="$t('pages.admin.user.add.subtitle')"
    />

    <personal-info :user="user" newUser />
    <user-groups
      :choosedIds="choosedIds"
      @update-choosed="updateChoosed"
      edit
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
import PersonalInfo from '@/components/user/PersonalInfo'
import UserGroups from '@/components/user/UserGroups'

import { showError } from '@/plugins/global'
export default {
  components: { PageTitle, PersonalInfo, UserGroups },
  data() {
    return {
      choosedIds: [],
      user: {},
      originalUser: {}
    }
  },

  methods: {
    reset() {
      this.user.email = ''
      this.user.name = ''
    },
    updateChoosed(ids) {
      this.choosedIds = ids
    },
    save() {
      const url = '/api/v1/users/'
      this.user.groups = this.choosedIds
      this.user.username = this.user.email
      this.$axios
        .$post(url, this.user)
        .then(res => {
          this.$toasted.global.defaultSuccess()
          this.$router.push({
            name: `admin___${this.$i18n.locale}`
          })
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
