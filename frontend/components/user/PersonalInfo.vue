<template>
  <div class="tile is-parent">
    <div class="tile is-child is-3">
      <strong>Configurações pessoais</strong>
    </div>
    <div class="tile is-child is-8">
      <input v-if="!newUser" id="user-id" v-model="user.id" type="hidden" />
      <b-field
        :label="$t('pages.admin.forms.email.label')"
        class="user-form-fields"
      >
        <b-input
          v-model="user.email"
          :placeholder="$t('pages.admin.forms.email.placeholder')"
          type="text"
          icon="tag"
          :disabled="!newUser"
          required
        />
      </b-field>
      <b-field
        :label="$t('pages.admin.forms.name.label')"
        class="user-form-fields"
      >
        <b-input
          v-model="user.name"
          :placeholder="$t('pages.admin.forms.name.placeholder')"
          type="text"
          icon="tag"
          required
        />
      </b-field>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    user: {
      type: Object,
      default() {
        return {}
      }
    },
    edit: {
      type: Boolean,
      default: false
    },
    newUser: {
      type: Boolean,
      default: false
    }
  }
}
</script>

<style></style>
