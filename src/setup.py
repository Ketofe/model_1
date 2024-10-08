from setuptools import setup, find_packages



setup(
   name="model1",
   py_modules=["Vicsek_modified","Vicsek_modified_conditional","order"],
   install_requires=["numpy","scipy"]
)



