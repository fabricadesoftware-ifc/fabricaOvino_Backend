<template>
  <div>
    <b-table striped :data="users">
      <template slot-scope="props">
        <b-table-column
          v-for="(column, index) in columns"
          :key="index"
          :field="column.field"
          :sortable="column.sortable"
          :label="column.label"
        >
          {{ props.row[column.field] }}
        </b-table-column>

        <b-table-column
          field="actions"
          :label="$t('pages.admin.breed.table.actions')"
        >
          <b-button type="is-warning" icon-left="pencil"> </b-button>
          <b-button type="is-danger" icon-left="trash-can-outline"> </b-button>
        </b-table-column>
      </template>
    </b-table>
  </div>
</template>

<script>
export default {
  data() {
    return {
      users: [],
      columns: [
        {
          field: 'id',
          label: this.$t('components.admin.useradmin.table.id'),
          sortable: true
        },
        {
          field: 'email',
          label: this.$t('components.admin.useradmin.table.email'),
          sortable: true
        },
        {
          field: 'name',
          label: this.$t('components.admin.useradmin.table.name'),
          sortable: true
        }
      ]
    }
  },
  async fetch() {
    this.users = await this.$axios.$get('/api/v1/users')
  }
}
</script>

<style></style>
