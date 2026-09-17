---
layout: default
title: Pyrazinamide
parent: 僅模型預測 (L5)
nav_order: 626
evidence_level: L5
indication_count: 5
---

# Pyrazinamide
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Pyrazinamide：從 結核病 到 感染性中耳炎 (Infectious Otitis Media)

## 一句話總結

Pyrazinamide 是治療結核病的一線藥物之一，為標準四合一抗結核方案（isoniazid + rifampin + pyrazinamide + ethambutol）的成分之一。
TxGNN 模型預測它可能對**感染性中耳炎 (Infectious Otitis Media)** 有效，預測分數高達 **99.96%**，
但目前**沒有任何臨床試驗或文獻**直接支持這個特定預測方向。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 結核病（四合一抗結核方案成分之一） |
| 預測新適應症 | 感染性中耳炎 (Infectious Otitis Media) |
| TxGNN 預測分數 | 99.96% |
| 證據等級 | L5 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

Pyrazinamide 是窄譜抗分枝桿菌前驅藥，經 *pncA* 基因編碼的 pyrazinamidase 轉化為活性態 pyrazinoic acid，僅在酸性的巨噬細胞內／乾酪性病灶環境中對結核分枝桿菌 (M. tuberculosis) 有效，並非廣效抗菌藥物。

「感染性中耳炎」一般指肺炎鏈球菌、流感嗜血桿菌、卡他莫拉菌等常見致病菌引起的中耳感染，與 pyrazinamide 的抗分枝桿菌機轉並無已知關聯，僅在病因為**結核性中耳炎**（tuberculous otitis media，肺外結核的罕見表現）時才可能相關。目前這個預測結果並未特指結核病因，故機轉上證據不足，TxGNN 的高分較可能反映知識圖譜中「otitis media」與「結核病」節點間的間接連結，而非藥物對此適應症的直接藥理作用。

值得注意的是，同一批預測中另有「chronic otitis media」與「suppurative otitis media」兩個相關病名，各有 8 篇與 5 篇文獻支持，但內容全部是**結核性中耳炎（TOM）病例報告**，並非一般感染性中耳炎的療效證據。這進一步印證：pyrazinamide 與「中耳炎」的關聯僅在結核病因成立時才有意義。

## 臨床試驗證據

目前無相關臨床試驗登記

## 文獻證據

目前無相關文獻

> 註：相關但不同病名的「chronic otitis media」「suppurative otitis media」預測項下各有結核性中耳炎（TOM）病例報告，可作為機轉層面的旁證，但不能視為「感染性中耳炎」本身的直接證據。

## 香港上市資訊

Pyrazinamide 目前**未在香港上市**，查無許可證資料。

## 安全性考量

安全性資訊請參考原廠仿單。

> 注意：仿單警語與禁忌症資料為 Blocking 等級資料缺口（DG001），在補齊前無法進行 S1 安全性初評。

## 結論與下一步

**決策：Hold**

**理由：**
TxGNN 分數雖然極高，但「感染性中耳炎」這個預測完全無臨床試驗或文獻支持，且 pyrazinamide 窄譜抗分枝桿菌的機轉與一般細菌性中耳炎缺乏藥理基礎，目前僅能視為知識圖譜的純預測訊號（L5 / S0）。

**若要推進需要：**
- 釐清目標族群是否為結核性中耳炎（TOM）——若是，建議改以「chronic otitis media」或「suppurative otitis media」作為研究方向，兩者已有 L4 等級的病例報告證據
- 補齊 TFDA／香港仿單警語與禁忌症資料（DG001，Blocking，阻擋 S1 安全性初評）
- 取得正式 DrugBank MOA 資料以確認機轉描述（DG002）
- 確認香港上市與許可證狀態
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

