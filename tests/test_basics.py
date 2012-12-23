import unittest
from jnius.reflect import autoclass

class BasicsTest(unittest.TestCase):

    def test_static_methods(self):
        Test = autoclass('org.jnius.BasicsTest')
        self.assertEquals(Test.methodStaticZ(), True)
        self.assertEquals(Test.methodStaticB(), 127)
        self.assertEquals(Test.methodStaticC(), 'k')
        self.assertEquals(Test.methodStaticS(), 32767)
        self.assertEquals(Test.methodStaticI(), 2147483467)
        self.assertEquals(Test.methodStaticJ(), 2147483467)
        self.assertAlmostEquals(Test.methodStaticF(), 1.23456789)
        self.assertEquals(Test.methodStaticD(), 1.23456789)
        self.assertEquals(Test.methodStaticString(), 'helloworld')

    def test_static_fields(self):
        Test = autoclass('org.jnius.BasicsTest')
        self.assertEquals(Test.fieldStaticZ, True)
        self.assertEquals(Test.fieldStaticB, 127)
        self.assertEquals(Test.fieldStaticC, 'k')
        self.assertEquals(Test.fieldStaticS, 32767)
        self.assertEquals(Test.fieldStaticI, 2147483467)
        self.assertEquals(Test.fieldStaticJ, 2147483467)
        self.assertAlmostEquals(Test.fieldStaticF, 1.23456789)
        self.assertEquals(Test.fieldStaticD, 1.23456789)
        self.assertEquals(Test.fieldStaticString, 'helloworld')

    def test_instance_methods(self):
        test = autoclass('org.jnius.BasicsTest')()
        self.assertEquals(test.methodZ(), True)
        self.assertEquals(test.methodB(), 127)
        self.assertEquals(test.methodC(), 'k')
        self.assertEquals(test.methodS(), 32767)
        self.assertEquals(test.methodI(), 2147483467)
        self.assertEquals(test.methodJ(), 2147483467)
        self.assertAlmostEquals(test.methodF(), 1.23456789)
        self.assertEquals(test.methodD(), 1.23456789)
        self.assertEquals(test.methodString(), 'helloworld')

    def test_instance_fields(self):
        test = autoclass('org.jnius.BasicsTest')()
        self.assertEquals(test.fieldZ, True)
        self.assertEquals(test.fieldB, 127)
        self.assertEquals(test.fieldC, 'k')
        self.assertEquals(test.fieldS, 32767)
        self.assertEquals(test.fieldI, 2147483467)
        self.assertEquals(test.fieldJ, 2147483467)
        self.assertAlmostEquals(test.fieldF, 1.23456789)
        self.assertEquals(test.fieldD, 1.23456789)
        self.assertEquals(test.fieldString, 'helloworld')

    def test_instances_methods_array(self):
        test = autoclass('org.jnius.BasicsTest')()
        self.assertEquals(test.methodArrayZ(), [True] * 3)
        self.assertEquals(test.methodArrayB(), [127] * 3)
        self.assertEquals(test.methodArrayC(), ['k'] * 3)
        self.assertEquals(test.methodArrayS(), [32767] * 3)
        self.assertEquals(test.methodArrayI(), [2147483467] * 3)
        self.assertEquals(test.methodArrayJ(), [2147483467] * 3)

        ret = test.methodArrayF()
        ref = [1.23456789] * 3
        self.assertAlmostEquals(ret[0], ref[0])
        self.assertAlmostEquals(ret[1], ref[1])
        self.assertAlmostEquals(ret[2], ref[2])

        self.assertEquals(test.methodArrayD(), [1.23456789] * 3)
        self.assertEquals(test.methodArrayString(), ['helloworld'] * 3)

    def test_instances_methods_params(self):
        test = autoclass('org.jnius.BasicsTest')()
        self.assertEquals(test.methodParamsZBCSIJFD(
            True, 127, 'k', 32767, 2147483467, 2147483467, 1.23456789, 1.23456789), True)
        self.assertEquals(test.methodParamsString('helloworld'), True)
        self.assertEquals(test.methodParamsArrayI([1, 2, 3]), True)
        self.assertEquals(test.methodParamsArrayString([
            'hello', 'world']), True)

    def test_instances_methods_params_object_list_str(self):
        test = autoclass('org.jnius.BasicsTest')()
        self.assertEquals(test.methodParamsObject([
            'hello', 'world']), True)

    def test_instances_methods_params_object_list_int(self):
        test = autoclass('org.jnius.BasicsTest')()
        self.assertEquals(test.methodParamsObject([1, 2]), True)

    def test_instances_methods_params_object_list_float(self):
        test = autoclass('org.jnius.BasicsTest')()
        self.assertEquals(test.methodParamsObject([3.14, 1.61]), True)

    def test_instances_methods_params_object_list_long(self):
        test = autoclass('org.jnius.BasicsTest')()
        self.assertEquals(test.methodParamsObject([1L, 2L]), True)

    def test_return_array_as_object_array_of_strings(self):
        test = autoclass('org.jnius.BasicsTest')()
        self.assertEquals(test.methodReturnStrings(), ['Hello', 'world'])

    def test_return_array_as_object_of_integers(self):
        test = autoclass('org.jnius.BasicsTest')()
        print 'begin'
        c = test.methodReturnIntegers()
        print 'end'
        self.assertEquals(c, [1, 2])
