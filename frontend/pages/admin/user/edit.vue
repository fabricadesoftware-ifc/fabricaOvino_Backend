<template>
  <div class="user-edit">
    <PageTitle
      icon="face"
      :main="$t('pages.admin.user.edit.title')"
      :sub="$t('pages.admin.user.edit.subtitle')"
    />

    <div class="form">
      <input type="hidden" id="user-id" v-model="user.id" />
      <b-field
        :label="$t('pages.admin.forms.name.label')"
        class="user-form-fields"
      >
        <b-input
          :placeholder="$t('pages.admin.forms.name.placeholder')"
          type="text"
          icon="tag"
          v-model="user.name"
          required
        />
      </b-field>
      <div class="user-form-buttons">
        <b-button type="is-info" icon-left="check" @click="save">
          {{ $t('buttons.save') }}
        </b-button>
        <b-button type="is-dark" icon-left="redo" @click="reset">
          {{ $t('buttons.reset') }}
        </b-button>
      </div>
    </div>
  </div>
</template>

<script>
import PageTitle from '@/components/templates/PageTitle'
import { showError } from '@/plugins/global'
export default {
  components: { PageTitle },
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
        .then(() => {
          this.$toasted.global.defaultSuccess()
          this.reset()
        })
        .catch(showError)
    }
  }
}
</script>

<style></style>
