<template>
  <div class="group-edit">
    <title-bar :title-stack="titleStack" />
    <hero-bar>
      {{ $t('pages.admin.group.edit.title') }}
      <template v-slot:right>
        <router-link to="/" class="button"> Dashboard </router-link>
      </template>
    </hero-bar>
    <!-- <PageTitle
      icon="face"
      :main="$t('pages.admin.group.edit.title')"
      :sub="$t('pages.admin.group.edit.subtitle')"
    /> -->
    <card-component>
      <general-info :group="group" edit />
      <permissions
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
import GeneralInfo from '@/components/group/GeneralInfo'
import Permissions from '@/components/group/Permissions'

export default {
  components: { TitleBar, HeroBar, CardComponent, GeneralInfo, Permissions },
  async fetch() {
    this.group = this.$route.params.group
    Object.assign(this.originalGroup, this.group)
    this.choosedIds = this.group.permissions.map(({ id }) => id)
  },
  data() {
    return {
      choosedIds: [],
      group: {},
      originalGroup: {}
    }
  },
  computed: {
    titleStack() {
      return ['Admin', this.$t('pages.admin.subtitle')]
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
      const id = this.group.id
      this.group.permissions = this.choosedIds
      const url = `/api/v1/groups/${id}/`
      this.$axios
        .$put(url, this.group)
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
