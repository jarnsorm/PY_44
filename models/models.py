import datetime
from typing import Annotated

from sqlalchemy import MetaData, ForeignKey, String, Numeric
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase, relationship

metadata = MetaData()

intpk = Annotated[int, mapped_column(primary_key=True)]
str20 = Annotated[str, 20]
mon = Annotated[Numeric, 12, 2]
ph_n = Annotated[Numeric, 10, 0]


class Base(DeclarativeBase):
    type_annotation_map = {
        str20: String(20),
        mon: Numeric(12, 2),
        ph_n: Numeric(10,0)
    }


class Employees(Base):
    __tablename__ = 'employees'

    id: Mapped[intpk]
    last_name: Mapped[str20]
    first_name: Mapped[str20]
    patronymic: Mapped[str20 | None]
    position: Mapped[str]
    address: Mapped[str]
    phone_number: Mapped[ph_n] = mapped_column(unique=True)
    DOB: Mapped[datetime.date]

    order = relationship('Orders', backref='empoloyees')


class Clients(Base):
    __tablename__ = 'clients'

    id: Mapped[intpk]
    full_name: Mapped[str]
    address: Mapped[str]
    phone_number: Mapped[ph_n] = mapped_column(unique=True)

    order = relationship('Orders', backref='clients')


class Providers(Base):
    __tablename__ = 'providers'

    id: Mapped[intpk]
    company_name: Mapped[str] = mapped_column(unique=True)
    contact_person: Mapped[str]
    phone_number: Mapped[ph_n] = mapped_column(unique=True)
    address: Mapped[str]

    delivery = relationship('Deliveries', backref='providers')


class Deliveries(Base):
    __tablename__ = 'deliveries'

    id: Mapped[intpk]
    provider_id = mapped_column(ForeignKey('providers.id'))
    date: Mapped[datetime.date]

    product = relationship('Products', backref='deliveries')


class Products(Base):
    __tablename__ = 'products'

    id: Mapped[intpk]
    supply_id = mapped_column(ForeignKey('deliveries.id'))
    product_name: Mapped[str]
    specifications: Mapped[str]
    description: Mapped[str | None]
    picture: Mapped[str | None]
    purchase_price: Mapped[mon]
    availability_in_stock: Mapped[int]
    quantity: Mapped[int]
    retail_price: Mapped[mon]

    order = relationship('Orders', backref='products')


class Orders(Base):
    __tablename__ = 'orders'

    id: Mapped[intpk]
    worker_id = mapped_column(ForeignKey('employees.id'))
    product_id = mapped_column(ForeignKey('products.id'))
    order_placement_date: Mapped[datetime.date]
    order_execution_date: Mapped[datetime.date]
    client_id = mapped_column(ForeignKey('clients.id'))