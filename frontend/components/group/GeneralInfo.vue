<template>
  <div class="tile is-parent">
    <div class="tile is-child is-3">
      <strong>{{ $t('components.group.generalInfo.title') }}</strong>
    </div>
    <div class="tile is-child is-8">
      <input id="group-id" v-model="group.id" type="hidden" />
      <b-field
        :label="$t('pages.admin.forms.name.label')"
        class="group-form-fields"
      >
        <b-input
          v-if="edit"
          v-model="group.name"
          :placeholder="$t('pages.admin.forms.name.placeholder')"
          type="text"
          icon="tag"
          required
        />
        <span v-else>{{ group.name }}</span>
      </b-field>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    group: {
      type: Object,
      default() {
        return {}
      }
    },
    edit: {
      type: Boolean,
      default: false
    }
  }
}
</script>

<style></style>
