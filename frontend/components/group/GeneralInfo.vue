<template>
  <div class="tile is-parent">
    <div class="tile is-child is-3">
      <strong>{{$t('components.group.generalInfo.title')}}</strong>
    </div>
    <div class="tile is-child is-8">
      <input type="hidden" id="group-id" v-model="group.id" />
      <b-field :label="$t('pages.admin.forms.name.label')" class="group-form-fields">
        <b-input
          v-if="edit"
          :placeholder="$t('pages.admin.forms.name.placeholder')"
          type="text"
          icon="tag"
          v-model="group.name"
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
    group: Object,
    edit: {
      type: Boolean,
      default () {
        return false
      }
    }
  }
}
</script>

<style>
</style>
