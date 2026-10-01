---
layout: default
title: Albutrepenonacog Alfa
parent: 僅模型預測 (L5)
nav_order: 29
evidence_level: L5
indication_count: 6
---

# Albutrepenonacog Alfa
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Albutrepenonacog alfa：從血友病 B 到類血友病性血管性假性疾病 (Pseudo-von Willebrand Disease)

## 一句話總結

Albutrepenonacog alfa 是重組第九凝血因子與白蛋白的融合蛋白（品牌名 IDELVION），一般用於血友病 B。Evidence Pack 並未載明原適應症，此為依藥物屬性的推定。
TxGNN 預測它可能對**假性血管性血友病 (Pseudo-von Willebrand Disease)** 有效，但目前**沒有任何臨床試驗或文獻**支持，只有模型預測。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 資料未載明（香港許可證的適應症欄位皆為空白；依藥物屬性推定為血友病 B） |
| 預測新適應症 | 假性血管性血友病 (Pseudo-von Willebrand Disease) |
| TxGNN 預測分數 | 99.94% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 4 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。Albutrepenonacog alfa 是重組第九因子融合蛋白，作用是補充缺乏的第九因子，支持內源性凝血路徑。

假性血管性血友病是血小板型疾病，成因是血小板 GPIbα 功能增強，過度結合 VWF。這類患者並不缺乏第九因子，補充第九因子無法處理根本缺陷。

因此，99.94% 的高分較可能反映知識圖譜中，這個藥物與凝血、出血相關節點距離接近，而不是已驗證的機轉。**這個預測在機轉上缺乏支持。**

### 其他預測適應症（同樣僅為模型預測）

| 排名 | 預測適應症 | TxGNN 分數 | 機轉評估 |
|------|-----------|-----------|---------|
| 2 | 血小板原發性釋放障礙 | 99.94% | 缺陷在血小板分泌功能，補充第九因子無法矯正 |
| 3 | Glanzmann 血小板無力症 | 99.92% | 缺陷在 GPIIb/IIIa，標準處置為血小板輸注或旁路藥物 |
| 4 | Scott 症候群 | 99.63% | 與 tenase 複合體有概念上的關聯，但缺陷在血小板表面，屬推測 |
| 5 | 膠原蛋白受體缺陷所致出血體質 | 99.28% | 缺陷在血小板受體功能，與第九因子無關 |
| 6 | 先天性血小板減少所致出血性疾病 | 99.26% | 問題在血小板數量或功能，且可能增加血栓風險 |

---

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

---

## 香港上市資訊

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-65142 | IDELVION Powder and Solvent for Solution for Injection 250IU | CSL Behring Asia Pacific Limited |
| HK-65143 | IDELVION Powder and Solvent for Solution for Injection 500IU | CSL Behring Asia Pacific Limited |
| HK-65144 | IDELVION Powder and Solvent for Solution for Injection 1000IU | CSL Behring Asia Pacific Limited |
| HK-65145 | IDELVION Powder and Solvent for Solution for Injection 2000IU | CSL Behring Asia Pacific Limited |

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 6 個預測適應症全都是 L5，沒有臨床試驗或文獻。
- 這些疾病的缺陷都在血小板或 VWF，第九因子並不缺乏，補充它在機轉上不合理。
- 補充第九因子還可能增加血栓風險，卻沒有明確的療效依據。

**若要推進需要：**
- 補齊香港衛生署仿單的警語與禁忌資料，並確認原核准適應症。
- 取得 DrugBank 的作用機轉資料。
- 找到能說明第九因子如何影響血小板功能缺陷的機轉或前臨床證據。若找不到，建議不再優先推進這些預測。

> 本報告結果僅供研究參考，不構成醫療建議。老藥新用候選需經過臨床驗證才能應用。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

