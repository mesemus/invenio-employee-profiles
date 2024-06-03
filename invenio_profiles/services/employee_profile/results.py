# -*- coding: utf-8 -*-
#
# Copyright (C) 2022 TU Wien.
#
# Invenio-Users-Resources is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.
"""Result Classes for representing Employee Profiles to user."""

from invenio_records_resources.services.base import ServiceItemResult, ServiceListResult


class RecordView(ServiceItemResult):
    """Record View of EmployeeProfile Model."""

    def __init__(self, identity, record):
        """Recordview initialization."""
        self._identity = identity
        self._record = record

    def to_dict(self):
        """Convert to dict."""
        return {
            "email_address": self._record.email_address,
            "biography": self._record.biography,
        }


# class RecordList(ServiceListResult):
#     """List of records result."""

#     def __init__(
#         self,
#         service,
#         identity,
#         results,
#         # params=None,
#         # links_tpl=None,
#         # links_item_tpl=None,
#         # nested_links_item=None,
#         # schema=None,
#         # expandable_fields=None,
#         # expand=False,
#     ):
#         """Constructor.

#         :params service: a service instance
#         :params identity: an identity that performed the service request
#         :params results: the search results
#         :params params: dictionary of the query parameters
#         """
#         self._identity = identity
#         self._results = results
#         self._service = service
#         # self._schema = schema or service.schema
#         # self._params = params
#         # self._links_tpl = links_tpl
#         # self._links_item_tpl = links_item_tpl
#         # self._nested_links_item = nested_links_item
#         # self._fields_resolver = FieldsResolver(expandable_fields)
#         # self._expand = expand

#     def __len__(self):
#         """Return the total numer of hits."""
#         return self.total

#     def __iter__(self):
#         """Iterator over the hits."""
#         return self.hits

#     @property
#     def total(self):
#         """Get total number of hits."""
#         if hasattr(self._results, "hits"):
#             return self._results.hits.total["value"]
#         else:
#             # handle scan(): returns a generator
#             return None

#     @property
#     def aggregations(self):
#         """Get the search result aggregations."""
#         # TODO: have a way to label or not label
#         try:
#             return self._results.labelled_facets.to_dict()
#         except AttributeError:
#             return None

#     @property
#     def hits(self):
#         """Iterator over the hits."""
#         for hit in self._results:
#             # Load dump
#             record = self._service.record_cls.loads(hit.to_dict())

#             # Project the record
#             projection = self._schema.dump(
#                 record,
#                 context=dict(
#                     identity=self._identity,
#                     record=record,
#                 ),
#             )
#             if self._links_item_tpl:
#                 projection["links"] = self._links_item_tpl.expand(
#                     self._identity, record
#                 )
#             if self._nested_links_item:
#                 for link in self._nested_links_item:
#                     link.expand(self._identity, record, projection)

#             yield projection

#     @property
#     def pagination(self):
#         """Create a pagination object."""
#         return Pagination(
#             self._params["size"],
#             self._params["page"],
#             self.total,
#         )

#     def to_dict(self):
#         """Return result as a dictionary."""
#         # TODO: This part should imitate the result item above. I.e. add a
#         # "data" property which uses a ServiceSchema to dump the entire object.
#         hits = list(self.hits)

#         if self._expand and self._fields_resolver:
#             self._fields_resolver.resolve(self._identity, hits)
#             for hit in hits:
#                 fields = self._fields_resolver.expand(self._identity, hit)
#                 hit["expanded"] = fields

#         res = {
#             "hits": {
#                 "hits": hits,
#                 "total": self.total,
#             }
#         }

#         if self.aggregations:
#             res["aggregations"] = self.aggregations

#         if self._params:
#             res["sortBy"] = self._params["sort"]
#             if self._links_tpl:
#                 res["links"] = self._links_tpl.expand(self._identity, self.pagination)

#         return res