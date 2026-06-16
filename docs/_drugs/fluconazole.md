---
layout: default
title: Fluconazole
parent: 僅模型預測 (L5)
nav_order: 321
evidence_level: L5
indication_count: 1
---

# Fluconazole
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Fluconazole：從抗真菌到點狀上皮角結膜炎

## 一句話總結

Fluconazole 是 azole 類廣效抗真菌藥，藉由阻斷真菌麥角固醇合成發揮作用，臨床上廣泛用於全身性及局部真菌感染的治療。
TxGNN 模型預測它可能對**點狀上皮角結膜炎（Punctate Epithelial Keratoconjunctivitis，PEK）**有效，預測分數高達 **99.24%**。
然而，目前**無任何臨床試驗或文獻**支持此方向，證據僅止於模型推測。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 真菌感染（抗真菌藥，依 DrugBank 分類） |
| 預測新適應症 | 點狀上皮角結膜炎 (Punctate Epithelial Keratoconjunctivitis) |
| TxGNN 預測分數 | 99.24% |
| 證據等級 | L5 |
| 香港上市 | ✗ 未上市（本批資料未收錄） |
| 許可證數 | 0 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

Fluconazole 為 azole 類抗真菌藥，藉由抑制真菌 CYP51A1（lanosterol 14α-demethylase）阻斷麥角固醇合成，破壞真菌細胞膜完整性。由於口服生物可用率約 90%，全身吸收良好，理論上藥物可透過血-眼屏障在房水中達到有效濃度，具備眼部感染治療的生理基礎。

點狀上皮角結膜炎（PEK）是角膜上皮出現多灶性點狀混濁的臨床表型，病因以腺病毒、HSV、乾眼症及 Thygeson's SPK 等為主；真菌性 PEK 屬罕見亞型，多見於免疫功能低下或手術後患者。TxGNN 的高分推測來自知識圖譜路徑：Fluconazole → 抗真菌機轉 → 真菌性角膜炎 → 角結膜炎表型 → PEK，屬間接推斷路徑。

此機轉連結的特異性不足：PEK 的主流病因並非真菌，fluconazole 對非真菌性 PEK 無直接作用機轉支持。目前臨床資料完全缺如，無法驗證模型預測的臨床意義。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

---

## 香港上市資訊

本批資料未收錄香港上市許可證（market_status：未上市，許可證數：0）。Fluconazole 於各主要市場均有廣泛上市產品，建議另行查閱香港衛生署藥物辦公室資料庫確認實際上市狀態。

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
TxGNN 預測分數雖高（99.24%），但點狀上皮角結膜炎並非真菌性疾病的主流表型，機轉連結屬間接推斷，且臨床試驗與文獻證據完全缺如（L5），現階段不具備推進條件。

**若要推進需要：**
- 確認目標族群：聚焦「真菌性 PEK」此一罕見亞型（免疫低下 / 術後患者），而非所有 PEK
- 補充基礎證據：搜尋 fluconazole 用於真菌性角膜炎 / 角結膜炎的相關病例報告或觀察性研究
- 確認香港上市狀態：查閱衛生署資料庫，補齊許可證及仿單警語資訊（DG001）
- 補充 MOA 詳細資料：查詢 DrugBank API 取得完整藥理機轉（DG002）
- 若基礎依據確立後，再考慮設計針對真菌性 PEK 的前瞻性觀察性研究
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

