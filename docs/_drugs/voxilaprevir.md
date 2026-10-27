---
layout: default
title: Voxilaprevir
parent: 僅模型預測 (L5)
nav_order: 943
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
description: "Voxilaprevir：預測新適應症為B 型肝炎病毒感染 (Hepatitis B Virus Infection)（證據等級 L5）。原適應症：慢性 C 型肝炎病毒感染 (chronic hepatitis C virus infection)"
monitor_inn: "VOXILAPREVIR"
predicted_indications: ["hepatitis B virus infection", "hepatitis E virus infection", "hepatitis, viral, animal", "hepatitis A virus infection", "Omsk hemorrhagic fever"]
---

# Voxilaprevir
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## 藥師評估報告

</div>

## Voxilaprevir：從慢性 C 型肝炎到 B 型肝炎病毒感染
{: .text-alpha }

## 一句話總結

Voxilaprevir 是 HCV NS3/4A 蛋白酶抑制劑，原本用於慢性 C 型肝炎，目前在香港以複方 VOSEVI 上市。
TxGNN 模型預測它可能對 **B 型肝炎病毒感染 (Hepatitis B Virus Infection)** 有效，但目前**沒有相關臨床試驗**，且**文獻中沒有任何一篇顯示它具抗 B 型肝炎活性**，實質上僅為模型預測。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 慢性 C 型肝炎病毒感染 (chronic hepatitis C virus infection) |
| 預測新適應症 | B 型肝炎病毒感染 (Hepatitis B Virus Infection) |
| TxGNN 預測分數 | 99.84% |
| 證據等級 | L5（僅有模型預測，無直接支持的研究） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 1 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。已知 Voxilaprevir 是 HCV NS3/4A 蛋白酶抑制劑，在 C 型肝炎中的療效已被證實（通常與 sofosbuvir、velpatasvir 組成複方使用）。

不過，從機轉上看，B 型肝炎病毒沒有 NS3/4A 蛋白酶的同源物，其複製依賴反轉錄酶，因此直接抗病毒作用並不合理。TxGNN 的高分很可能反映的是「肝炎類疾病」在知識圖譜網絡上的鄰近性，而非共同的藥物標靶。

唯一的間接關聯是 B 型與 C 型肝炎共同感染的族群，以及 C 型肝炎直接作用抗病毒藥物（DAA）治療期間可能發生的 B 型肝炎再活化風險。這屬於安全性議題，不是療效證據。

其他預測適應症（E 型肝炎、動物病毒性肝炎、A 型肝炎、鄂木斯克出血熱）同樣僅為模型預測，證據等級皆為 L5，機轉上也缺乏支持。

---

## 臨床試驗證據

目前無與 B 型肝炎相關的臨床試驗登記。

另有 7 個試驗是透過資料庫關聯被配對到 A 型肝炎這個預測項目，但皆為 voxilaprevir 的 C 型肝炎或肝癌研究，與 B 型肝炎無關，故不列入。

---

## 文獻證據

下列 9 篇文獻皆與 C 型肝炎的再治療、抗藥性、藥動學、價格或血源性感染流行病學有關，**沒有一篇顯示 voxilaprevir 對 B 型肝炎有活性**。

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [35248212](https://pubmed.ncbi.nlm.nih.gov/35248212/) | 2022 | 單臂試驗（Cohort） | Lancet Gastroenterol Hepatol | 在盧安達，針對先前 DAA 治療失敗的 C 型肝炎患者，評估 sofosbuvir-velpatasvir-voxilaprevir 再治療的安全性與療效 |
| [36535062](https://pubmed.ncbi.nlm.nih.gov/36535062/) | 2022 | Cohort | J Gastrointestin Liver Dis | 羅馬尼亞 1b 型 HCV 對 DAA 無反應者的真實世界再治療 |
| [40611935](https://pubmed.ncbi.nlm.nih.gov/40611935/) | 2025 | Cohort | J Clin Exp Hepatol | DAA 治療後抗藥性相關突變與治療失敗的預測因子 |
| [31041789](https://pubmed.ncbi.nlm.nih.gov/31041789/) | 2019 | Review | Semin Liver Dis | DAA 治療失敗的 C 型肝炎患者之再治療 |
| [31114957](https://pubmed.ncbi.nlm.nih.gov/31114957/) | 2019 | Review | Clin Pharmacokinet | C 型肝炎治療的藥動學與藥效學考量（2019 更新） |
| [29369303](https://pubmed.ncbi.nlm.nih.gov/29369303/) | 2018 | Review | AIDS Rev | 2017 國際病毒性肝炎會議報告 |
| [30964552](https://pubmed.ncbi.nlm.nih.gov/30964552/) | 2019 | 前臨床/病毒學 | Hepatology | HCV 蛋白酶抑制劑逃逸變異株的演化路徑 |
| [40414600](https://pubmed.ncbi.nlm.nih.gov/40414600/) | 2025 | 其他（價格分析） | Ann Hepatol | B 型與 C 型肝炎藥物價格的全球比較 |
| [41570233](https://pubmed.ncbi.nlm.nih.gov/41570233/) | 2025 | 橫斷面研究 | Vopr Virusol | 牙科診療中 HIV、HBV、HCV 標記的盛行率與病毒株分析 |

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-65775 | VOSEVI TABLETS | 未提供 | 未提供 |

製造商為 GILEAD SCIENCES HONG KONG LIMITED，狀態為有效，屬單一成分許可證。

---

## 安全性考量

- **藥物交互作用**：已查詢到 19 筆交互作用，其中 **Major（重大）** 包括：
  - Rosuvastatin
  - Edoxaban
  - Cyclosporine

  其餘 16 筆為 Moderate（中度），例如 Apixaban、Cobicistat、Ethinylestradiol、Lapatinib、Lenvatinib、Olaparib、Pazopanib、Teriflunomide 等。

其餘警語與禁忌症資料，請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- B 型肝炎沒有 NS3/4A 蛋白酶這個標靶，機轉上不合理，且無任何臨床試驗或文獻支持。TxGNN 高分更可能反映網絡鄰近性。
- 其他預測適應症也僅為模型預測（L5），目前不建議投入資源。

**若要推進需要：**
- 補齊 voxilaprevir 的作用機轉資料（DrugBank）與香港仿單的警語及禁忌症。
- 進行體外試驗，確認對 HBV 複製是否有任何活性。
- 若要探討臨床相關性，可改為研究 HBV/HCV 共同感染族群中的 HBV 再活化風險與監測，這屬於安全性研究。
- 在 Omsk 出血熱等黃病毒科疾病，可先以體外蛋白酶抑制試驗檢驗，再決定是否值得進一步評估。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

