<template>
  <div class="user-edit">
    <PageTitle
      icon="face"
      :main="$t('pages.admin.user.edit.title')"
      :sub="$t('pages.admin.user.edit.subtitle')"
    />

    <avatar :email="user.email" />
    <personal-info :user="user" />

    <div class="form-bottons columns is-mobile is-centered">
      <div class="column is-4">
        <b-button type="is-info" icon-left="check" @click="save">{{ $t('buttons.save') }}</b-button>
        <b-button type="is-dark" icon-left="redo" @click="reset">{{ $t('buttons.reset') }}</b-button>
      </div>
    </div>
  </div>
</template>

<script>
import PageTitle from '@/components/templates/PageTitle'
import Avatar from '@/components/user/Avatar'
import PersonalInfo from '@/components/user/PersonalInfo'
import ChangePassword from '@/components/user/ChangePassword'
import { showError } from '@/plugins/global'
export default {
  components: { Avatar, ChangePassword, PersonalInfo, PageTitle },
  fetch() {
    this.user = this.$route.params.user
    Object.assign(this.originalUser, this.user)
  },
  data() {
    return {
      user: {},
      originalUser: {}
    }
  },

  methods: {
    reset() {
      Object.assign(this.user, this.originalUser)
    },
    save() {
      const id = this.user.id
      const url = `/api/v1/users/${id}/`
      this.$axios
        .$put(url, this.user)
        .then(res => {
          this.$toasted.global.defaultSuccess()
          this.reset()
          sthis.user = res
        })
        .catch(showError)
    }
  }
}
</script>

<style>
.form-bottons {
  margin-top: 20px;
}
</style>
