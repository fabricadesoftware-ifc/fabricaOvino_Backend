<template>
  <div>
    <b-button
      v-if="!deleteMode"
      type="is-primary"
      tag="nuxt-link"
      :to="localePath({ name: 'admin-group-add' })"
      icon-left="account-group"
    >{{$t('components.admin.groupadmin.add')}}</b-button>
    <span v-else>
      <b-button
        type="is-danger"
        @click="deleteGroup()"
        icon-left="account-group"
      >{{$t('components.admin.groupadmin.confirmDeletion')}} - {{ groupToDelete.name }}</b-button>
    </span>
    <b-table striped :data="groups">
      <template slot-scope="props">
        <b-table-column
          v-for="(column, index) in columns"
          :key="index"
          :field="column.field"
          :sortable="column.sortable"
          :label="column.label"
        >{{ props.row[column.field] }}</b-table-column>

        <b-table-column field="actions" :label="$t('pages.admin.breed.table.actions')">
          <b-button type="is-warning" @click="editGroup(props.row)" icon-left="pencil"></b-button>
          <b-button type="is-danger" @click="deleteGroup(props.row)" icon-left="trash-can-outline"></b-button>
        </b-table-column>
      </template>
    </b-table>
    <b-button
      v-if="!deleteMode"
      type="is-primary"
      tag="nuxt-link"
      :to="localePath({ name: 'admin-group-add' })"
      icon-left="account-group"
    >{{$t('components.admin.groupadmin.add')}}</b-button>
    <span v-else>
      <b-button
        type="is-danger"
        @click="deleteGroup()"
        icon-left="account-group"
      >{{$t('components.admin.groupadmin.confirmDeletion')}} - {{ groupToDelete.name }}</b-button>
    </span>
  </div>
</template>

<script>
export default {
  data() {
    return {
      deleteMode: false,
      groupToDelete: '',
      groups: [],
      columns: [
        {
          field: 'id',
          label: this.$t('components.admin.useradmin.table.id'),
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
    this.groups = await this.$axios.$get('/api/v1/groups')
  },
  methods: {
    editGroup(group) {
      this.$router.push({
        name: `admin-group-edit___${this.$i18n.locale}`,
        params: { group }
      })
    },
    deleteGroup(group=this.groupToDelete) {
      if (!this.deleteMode) {
        this.groupToDelete = group
        this.deleteMode = true
      } else {
        let url = `/api/v1/groups/${this.groupToDelete.id}`
        this.groupToDelete = ''
        this.deleteMode = false
        this.$axios.$delete(url).then(() => {
          this.$toasted.global.defaultSuccess();
          this.$fetch()
        }).catch(e =>{
          for (var item in e.response.data) {
            this.$toast.error(item + ': ' +  e.response.data[item])
          }
        })
      }
    }
  }
}
</script>

<style>
table {
  padding: 20px 0px;
}
</style>
