<template>
  <div class="user-edit">
    <title-bar :title-stack="titleStack" />
    <hero-bar>
      {{ $t('pages.admin.user.add.title') }}
      <template v-slot:right>
        <router-link to="/" class="button"> Dashboard </router-link>
      </template>
    </hero-bar>
    <!-- <PageTitle
      icon="face"
      :main="$t('pages.admin.user.add.title')"
      :sub="$t('pages.admin.user.add.subtitle')"
    /> -->

    <card-component>
      <personal-info :user="user" new-user />
      <user-groups
        :choosed-ids="choosedIds"
        edit
        @update-choosed="updateChoosed"
      />
    </card-component>
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
import TitleBar from '@/components/templates/TitleBar'
import HeroBar from '@/components/templates/HeroBar'
import CardComponent from '@/components/templates/CardComponent'
import PersonalInfo from '@/components/user/PersonalInfo'
import UserGroups from '@/components/user/UserGroups'

export default {
  components: { TitleBar, HeroBar, CardComponent, PersonalInfo, UserGroups },
  data() {
    return {
      choosedIds: [],
      user: {},
      originalUser: {}
    }
  },
  computed: {
    titleStack() {
      return ['Admin', this.$t('pages.admin.subtitle')]
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
        .then(() => {
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
