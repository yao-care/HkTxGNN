---
layout: default
title: Propranolol
parent: 僅模型預測 (L5)
nav_order: 725
evidence_level: L5
indication_count: 6
---

# Propranolol
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

# Propranolol：從原適應症（資料未提供）到遠端肌病 Tateyama 型

## 一句話總結

Propranolol（DrugBank：DB00571）在香港已上市，但本次資料沒有記載原適應症。
TxGNN 模型預測它可能對**遠端肌病 Tateyama 型 (distal myopathy, Tateyama type)** 有效，
但目前**沒有任何臨床試驗或文獻**支持，僅是模型預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 香港許可證資料未載明 |
| 預測新適應症 | 遠端肌病 Tateyama 型 (distal myopathy, Tateyama type) |
| TxGNN 預測分數 | 99.40% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 17 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。Propranolol 一般已知為非選擇性 β 腎上腺素受體阻斷劑，但本次資料未收錄原適應症與正式 MOA，無法據此建立與肌病的機轉連結。

遠端肌病 Tateyama 型是罕見的遺傳性肌肉疾病。現有資料找不到 β 阻斷作用與這個疾病之間的合理關聯。
模型給出的 0.994 高分應視為知識圖譜的關聯推論，而非有生物學依據的結論。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

共 17 張許可證，以下列出 5 張。資料未提供劑型與核准適應症。

| 許可證號 | 品名 | 製造商 |
|---------|------|--------|
| HK-50454 | BETAPRESS 10 FC TAB 10MG | Natural Health Resources Company Limited |
| HK-45677 | BECARDIN 40 TAB 40MG | Healthcare Pharmascience Limited |
| HK-45676 | BECARDIN 10 TAB 10MG | Healthcare Pharmascience Limited |
| HK-33813 | DERALIN 10 TAB 10MG | Viatris Healthcare Hong Kong Limited |
| HK-16631 | PROPRANOLOL TAB 10MG | Kai Yuen Pharmaceutical Co |

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
這項預測只有模型分數，沒有試驗、文獻或機轉依據（L5），且原適應症與 MOA 資料都缺漏，不建議推進。

**若要推進需要：**
- 取得香港衛生署核准仿單，補齊原適應症、警語與禁忌症
- 從 DrugBank 補充 MOA，再評估與肌病的機轉關聯
- 針對 Tateyama 型遠端肌病做專門的文獻與機轉檢索

**補充：** 同一藥物的其他預測中，「肝硬化心肌病」與「心肌病」目前為 L3（建議 Research Question）。
前者有 propranolol 與肝硬化 QT 延長的 2024 年研究，也有晚期患者可能受害的訊號；後者主要是 HCM 的早期小型研究，β 阻斷劑在此已是既有療法，並非新的老藥新用訊號。若要投入資源，這兩項比本預測更值得優先追蹤。

> 本報告僅供研究參考，不構成醫療建議；老藥新用候選需經臨床驗證才能應用。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

