Stock Shipment Deviation
########################

When in a stock shipment out there are movements with more products than have
the sale order that generates it, Tryton's default behavior is to give away the
excess.

This module assigns the movement of stock which creates Tryton with the amount
sent minus the quantity of the sale order that generates it, and alerts the
user that the difference is normally invoiced. The invoice does not add any
additional line in it, but the single line includes the total amount of the
product shipped. 
