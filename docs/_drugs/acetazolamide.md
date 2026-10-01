---
layout: default
title: Acetazolamide
parent: 僅模型預測 (L5)
nav_order: 18
evidence_level: L5
indication_count: 10
---

# Acetazolamide
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Acetazolamide：預測新適應症為運動誘發惡性高熱

## 一句話總結

Acetazolamide（乙醯唑胺）是碳酸酐酶抑制劑，在香港已有 3 張上市許可證，但證據包中沒有記載原核准適應症。
TxGNN 模型預測它可能對**運動誘發惡性高熱 (Exercise-induced Malignant Hyperthermia)** 有效，但目前**沒有任何臨床試驗或文獻**支持，屬於純模型預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 預測新適應症 | 運動誘發惡性高熱 (Exercise-induced Malignant Hyperthermia) |
| TxGNN 預測分數 | 99.95% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 3 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（DrugBank 的 MOA 欄位為空）。已知 acetazolamide 抑制碳酸酐酶，並用於週期性麻痺等離子通道相關的肌肉疾病。

運動誘發惡性高熱與肌肉的鈣離子調控異常有關，模型可能因此把兩者聯繫起來。但這個連結目前只是推測，提供的資料中沒有任何證據支持 acetazolamide 對高熱或鈣調控相關肌病有效。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-50001 | ACETAZOLAMIDE 250 TAB 250MG (REMEDICA) | HEALTHCARE PHARMASCIENCE LIMITED |
| HK-36263 | APO-ACETAZOLAMIDE TAB 250MG | HIND WING CO LTD |
| HK-16895 | ACETAZOLAMIDE TAB 250MG (WHITE) | SYNCO (H.K.) LIMITED |

## 安全性考量

安全性資訊請參考原廠仿單。藥物交互作用查詢無結果。

## 結論與下一步

**決策：Hold**

**理由：**
- 首位預測只有模型分數（證據等級 L5），沒有試驗、文獻，也沒有可驗證的作用機轉，目前不適合推進。
- 同一份證據包中的其他預測也多為 L5，只有心肌病變（Cardiomyopathy，第 7 名）有較多訊號，見下方說明。

**其他預測的參考資訊：**
- **心肌病變 (Cardiomyopathy)**：有 3 個進行中的第四期或非藥物特定試驗（NCT05802849、NCT06092437、NCT06166654），但研究對象是急性心衰竭，不是心肌病變本身，且都尚無結果。證據等級為 L4，證據包建議列為研究問題。
- **腸阻塞 (Intestinal obstruction)** 與**偽性腸阻塞 (Intestinal pseudoobstruction)**：文獻反而顯示 acetazolamide 可能引起麻痺性腸阻塞，預測很可能是偽陽性。
- **肝硬化性心肌病變 (Cirrhotic cardiomyopathy)**：acetazolamide 可能在肝硬化患者誘發高血氨與腦病變，屬於安全性疑慮。

**若要推進需要：**
- 補齊 acetazolamide 的作用機轉資料（DrugBank）。
- 取得香港衛生署的仿單，包含警語與禁忌症，並補上各許可證的核准適應症。
- 針對運動誘發惡性高熱做系統性文獻檢索，確認有無機轉或病例證據。
- 若優先考慮心肌病變，待急性心衰竭試驗公布結果後，分析是否有心肌病變亞群的數據。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

