<template>
  <div class="tile is-parent">
    <div class="tile is-child is-3">
      <strong>Configurações pessoais</strong>
    </div>
    <div class="tile is-child is-8">
      <input v-if="!newUser" type="hidden" id="user-id" v-model="user.id" />
      <b-field
        :label="$t('pages.admin.forms.email.label')"
        class="user-form-fields"
      >
        <b-input
          :placeholder="$t('pages.admin.forms.email.placeholder')"
          type="text"
          icon="tag"
          :disabled="!newUser"
          v-model="user.email"
          required
        />
      </b-field>
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
    </div>
  </div>
</template>

<script>
export default {
  props: {
    user: Object,
    edit: {
      type: Boolean,
      default() {
        return false
      }
    },
    newUser: {
      type: Boolean,
      default() {
        return false
      }
    }
  }
}
</script>

<style></style>
