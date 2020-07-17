<template>
  <div class="user-edit">
    <title-bar :title-stack="titleStack" />
    <hero-bar>
      {{ $t('pages.admin.user.edit.title') }}
      <template v-slot:right>
        <div class="buttons">
          <b-button @click="editUser(user)">Editar Perfil</b-button>
          <b-button type="is-warning" @click="isChangingPassword = true"
            >Alterar Senha</b-button
          >
        </div>
      </template>
    </hero-bar>

    <b-modal
      :active.sync="isChangingPassword"
      has-modal-card
      trap-focus
      :destroy-on-hide="false"
      aria-role="dialog"
      aria-modal
    >
      <change-password
        :id="user.id"
        is-admin
        :email="user.email"
      ></change-password>
    </b-modal>

    <card-component title="Informações do usuário" icon="ballot">
      <avatar :email="user.email" />
      <personal-info :user="user" />
      <user-groups
        :choosed-ids="choosedIds"
        edit
        @update-choosed="updateChoosed"
      />
    </card-component>

    <div class="form-bottons columns is-mobile is-centered">
      <div class="column is-4">
        <b-button type="is-primary" icon-left="check" @click="save">{{
          $t('buttons.save')
        }}</b-button>
        <b-button
          type="is-primary is-outlined"
          icon-left="redo"
          @click="reset"
          >{{ $t('buttons.reset') }}</b-button
        >
      </div>
    </div>
  </div>
</template>

<script>
import TitleBar from '@/components/templates/TitleBar'
import HeroBar from '@/components/templates/HeroBar'
import CardComponent from '@/components/templates/CardComponent'
import Avatar from '@/components/user/Avatar'
import PersonalInfo from '@/components/user/PersonalInfo'
import ChangePassword from '@/components/user/ChangePassword'
import UserGroups from '@/components/user/UserGroups'

export default {
  components: {
    Avatar,
    ChangePassword,
    CardComponent,
    PersonalInfo,
    HeroBar,
    TitleBar,
    UserGroups
  },
  fetch() {
    this.user = this.$route.params.user
    Object.assign(this.originalUser, this.user)
  },
  data() {
    return {
      user: {},
      originalUser: {},
      choosedIds: [],
      isChangingPassword: false
    }
  },
  computed: {
    titleStack() {
      return ['Admin', this.$t('pages.me.title')]
    }
  },
  methods: {
    reset() {
      Object.assign(this.user, this.originalUser)
    },
    save() {
      const id = this.user.id
      this.user.groups = this.choosedIds
      const url = `/api/v1/users/${id}/`
      this.$axios
        .$put(url, this.user)
        .then(res => {
          this.$toasted.global.defaultSuccess()
          this.user = res
        })
        .catch(e => {
          for (var item in e.response.data) {
            this.$toast.error(e.response.data[item])
          }
        })
    },
    updateChoosed(ids) {
      this.choosedIds = ids
    }
  }
}
</script>

<style>
.form-bottons {
  margin-top: 20px;
}
</style>
