use comp_flow::*;
use numpy::{IntoPyArray, PyArray1, PyArrayDyn, PyReadonlyArray1, PyReadonlyArrayDyn};
use pyo3::prelude::*;

#[pyfunction]
fn To_T_from_Ma<'py>(
    py: Python<'py>,
    Ma: PyReadonlyArray1<f64>,
    ga: f64,
) -> Bound<'py, PyArray1<f64>> {
    Ma.as_array()
        .map(|&m| 1. / mach_to_t_t0(m, ga))
        .into_pyarray(py)
}

#[pyfunction]
fn Po_P_from_Ma<'py>(
    py: Python<'py>,
    Ma: PyReadonlyArray1<f64>,
    ga: f64,
) -> Bound<'py, PyArray1<f64>> {
    Ma.as_array()
        .map(|&m| 1. / mach_to_p_p0(m, ga))
        .into_pyarray(py)
}

#[pyfunction]
fn rhoo_rho_from_Ma<'py>(
    py: Python<'py>,
    Ma: PyReadonlyArrayDyn<f64>,
    ga: f64,
) -> Bound<'py, PyArrayDyn<f64>> {
    Ma.as_array()
        .map(|&m| 1. / mach_to_rho_rho0(m, ga))
        .into_pyarray(py)
}

#[pyfunction]
fn A_Acrit_from_Ma<'py>(
    py: Python<'py>,
    Ma: PyReadonlyArrayDyn<f64>,
    ga: f64,
) -> Bound<'py, PyArrayDyn<f64>> {
    Ma.as_array()
        .map(|&m| 1. / mach_to_a_ac(m, ga))
        .into_pyarray(py)
}

#[pyfunction]
fn Ma_from_To_T<'py>(
    py: Python<'py>,
    To_T: PyReadonlyArrayDyn<f64>,
    ga: f64,
) -> Bound<'py, PyArrayDyn<f64>> {
    To_T.as_array()
        .map(|&r| mach_from_t_t0(1. / r, ga))
        .into_pyarray(py)
}

#[pyfunction]
fn Ma_from_Po_P<'py>(
    py: Python<'py>,
    Po_P: PyReadonlyArrayDyn<f64>,
    ga: f64,
) -> Bound<'py, PyArrayDyn<f64>> {
    Po_P.as_array()
        .map(|&r| mach_from_p_p0(1. / r, ga))
        .into_pyarray(py)
}

#[pyfunction]
fn Ma_from_rhoo_rho<'py>(
    py: Python<'py>,
    rhoo_rho: PyReadonlyArrayDyn<f64>,
    ga: f64,
) -> Bound<'py, PyArrayDyn<f64>> {
    rhoo_rho
        .as_array()
        .map(|&r| mach_from_rho_rho0(1. / r, ga))
        .into_pyarray(py)
}

#[pyfunction]
fn Ma_from_A_Acrit<'py>(
    py: Python<'py>,
    A_Acrit: PyReadonlyArrayDyn<f64>,
    ga: f64,
    sup: Option<bool>,
) -> Bound<'py, PyArrayDyn<f64>> {
    let supersonic: bool = match sup {
        Some(x) => x,
        None => false,
    };
    A_Acrit
        .as_array()
        .map(|&r| mach_from_a_ac(r, ga, supersonic))
        .into_pyarray(py)
}

/// A Python module implemented in Rust.
#[pymodule]
fn compflow2(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(To_T_from_Ma, m)?)?;
    m.add_function(wrap_pyfunction!(Po_P_from_Ma, m)?)?;
    m.add_function(wrap_pyfunction!(rhoo_rho_from_Ma, m)?)?;
    m.add_function(wrap_pyfunction!(A_Acrit_from_Ma, m)?)?;
    m.add_function(wrap_pyfunction!(Ma_from_Po_P, m)?)?;
    m.add_function(wrap_pyfunction!(Ma_from_To_T, m)?)?;
    m.add_function(wrap_pyfunction!(Ma_from_rhoo_rho, m)?)?;
    m.add_function(wrap_pyfunction!(Ma_from_A_Acrit, m)?)?;
    Ok(())
}
