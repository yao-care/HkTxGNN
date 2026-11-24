---
layout: default
title: Dutasteride
parent: 僅模型預測 (L5)
nav_order: 305
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-24
description: "Dutasteride：預測新適應症為Ambras 型先天性全身性多毛症 (Ambras type hypertrichosis universalis congenita)（證據等級 L5）。原適應症：良性攝護腺增生 (benign prostatic hyperplasia)"
monitor_inn: "DUTASTERIDE"
predicted_indications: ["Ambras type hypertrichosis universalis congenita", "hypertrichosis (disease)", "malformation syndrome with odontal and/or periodontal component", "syndrome with a Dandy-Walker malformation as major feature", "isolated genetic hair shaft abnormality", "hypotrichosis simplex of the scalp", "congenital hypotrichosis milia", "diffuse alopecia areata", "migraine with brainstem aura", "familial isolated trichomegaly"]
---

# Dutasteride
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

## Dutasteride：從良性攝護腺增生到安布拉斯型全身性先天多毛症
{: .text-alpha }

## 一句話總結

Dutasteride 是一種 5-α 還原酶抑制劑，原本用於治療良性攝護腺增生。
TxGNN 模型預測它可能對 **Ambras 型先天性全身性多毛症 (Ambras type hypertrichosis universalis congenita)** 有效，
但目前**沒有任何臨床試驗或文獻**直接支持這個預測，僅屬模型推論。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 良性攝護腺增生 (benign prostatic hyperplasia) |
| 預測新適應症 | Ambras 型先天性全身性多毛症 (Ambras type hypertrichosis universalis congenita) |
| TxGNN 預測分數 | 1.0000 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 11 張／共 11 張） |
| 許可證數 | 11 張（有效 11 張） |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

根據美國 FDA 核准的 Dutasteride 處方資料（Prescribing Information）「Mechanism of Action」段（非官方翻譯）：「Dutasteride 抑制睪固酮轉化為 DHT。DHT 是主要負責前列腺最初發育及其後增大的雄性素。睪固酮經由 5α-還原酶轉化為 DHT，此酶有 2 種同功型：第 1 型及第 2 型。」英文原文："Dutasteride inhibits the conversion of testosterone to DHT. DHT is the androgen primarily responsible for the initial development and subsequent enlargement of the prostate gland. Testosterone is converted to DHT by the enzyme 5 alpha-reductase, which exists as 2 isoforms, type 1 and type 2."（[DailyMed: dutasteride prescribing information, Strides Pharma Science Limited](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=c78d18cf-05df-4154-b2f9-39cc374ca9e3)，版本日期 2026-08-27；查閱日期 2026-11-19）。就一般藥理知識而言，Dutasteride 是第 1 型與第 2 型 5-α 還原酶的雙重抑制劑，可降低二氫睪固酮 (DHT)，因此用於攝護腺增生，也常見於雄性禿的仿單外使用。

不過，Ambras 症候群是罕見的遺傳疾患（與 8q 染色體重排影響 TRPS1 調控有關），並非已知由雄性素驅動。因此兩者的機轉關聯很薄弱，此預測分數來自 TxGNN 模型（深度學習），可能只是反映模型學到的相關疾病（毛髮相關）之間的相似性，而非生物學證據。

其他排名靠前的預測（一般多毛症、毛髮軸異常、單純性頭皮毛髮稀少症等）也多半屬於毛髮主題的連結，同樣缺乏證據。部分預測（如牙周畸形症候群、Dandy-Walker 症候群）則找不到合理的機轉連結，分數來自 TxGNN 模型（深度學習），可能只是反映模型學到的疾病間相似性，而非生物學證據。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

針對首位預測（Ambras 型多毛症）目前無相關文獻。

作為參考，排名第 8 的預測「瀰漫性圓禿 (diffuse alopecia areata)」有一篇間接相關的文獻：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [41714473](https://pubmed.ncbi.nlm.nih.gov/41714473/) | 2026 | Review | American Journal of Clinical Dermatology | 女性雄性素性禿的敘述性回顧，涵蓋病理生理、臨床評估與治療；僅支持 Dutasteride 與雄性素性禿的關聯，不直接適用於圓禿（自身免疫性） |

---

## 香港上市資訊

香港含本藥成分的許可證包括單一成分與複方製劑（含與 tamsulosin 的複方；張數與有效張數見本頁快速總覽與「香港上市資訊」的許可證表），列出其中部分：

<!-- review:begin hk-lic-20261124b-dutasteride-1 -->

> **查核更正（2026-11-24）**：原文為「香港共有 11 張有效許可證（皆為單一成分登記，無已註銷者），列出其中 5 張：」。已更正：依衞生署藥物辦公室註冊名單的成分欄，含本藥成分的許可證包括單一成分與複方製劑；原句的單一成分／複方說法或張數跟註冊名單不符（舊報告依證據包以「;;」切成分，每張都算成單方）。張數見本頁快速總覽與許可證表（2026-11-24 核對）。依據：[衞生署藥物辦公室：藥劑製品註冊名單（DrugList.xml，data.gov.hk；證據包 Release data-20261123-235245）](https://www.drugoffice.gov.hk/eps/psi/DrugList.xml)。

<!-- review:end hk-lic-20261124b-dutasteride-1 -->

<!-- licenses:begin -->

| 許可證號 | 品名 | 類別 | 持證商 | 狀態 |
|------|------|------|------|------|
| HK-61577 | AVODART CAPSULES 0.5MG | 單一成分 | GLAXOSMITHKLINE LIMITED | 有效 |
| HK-64673 | APO-DUTASTERIDE CAPSULES 0.5MG | 單一成分 | HIND WING CO LTD | 有效 |
| HK-68564 | DUTASTERIDE SANDOZ CAPSULES 0.5MG | 單一成分 | SANDOZ HONG KONG LIMITED | 有效 |
| HK-61184 | DUODART CAPSULE 0.5MG/0.4MG | 複方 | GLAXOSMITHKLINE LIMITED | 有效 |
| HK-68297 | DUTASTERIDE/TAMSULOSIN HYDROCHLORIDE SANDOZ CAPSULES 0.5MG/0.4MG | 複方 | SANDOZ HONG KONG LIMITED | 有效 |

上表列出其中 5 張（共 11 張）。

<!-- licenses:end -->

---

## 安全性考量

- **知識圖譜標示的相關禁忌疾病**：多發性系統萎縮、姿勢性姿態心搏過速症候群 (POTS)、姿勢性低血壓、肝病、膽囊疾病、陰莖異常勃起、術中虹膜鬆弛症候群 (IFIS)。此為知識圖譜的藥物—疾病關聯，並非仿單文字，需以仿單確認。
- **藥物交互作用**：共查得 100 筆，以下為主要的中度交互作用：
  - Aprepitant
  - Cimetidine
  - Clarithromycin
  - Clotrimazole
  - Miconazole

  其餘多筆（如 Omeprazole、Metformin、Simvastatin、Prednisone 等）交互作用等級未明。
- **發育安全疑慮**：5-α 還原酶抑制可能影響發育過程，若考慮用於先天性或發育性疾病，需特別謹慎。

仿單的警語與禁忌資料請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 預測分數雖高（1.0000），但沒有任何臨床試驗或文獻佐證，證據等級僅 L5。
- Ambras 症候群並非雄性素驅動的疾病，機轉連結只是推測；前十名預測也多為毛髮主題，其分數來自 TxGNN 模型（深度學習），可能反映模型學到的相關疾病相似性，而非生物學證據，缺乏實質治療依據。

**若要推進需要：**
- 補充 Dutasteride 的作用機轉資料（DrugBank）。
- 取得香港衛生署的仿單，確認警語、禁忌與核准適應症。
- 進行機轉層面的文獻回顧，確認 DHT 在 Ambras 症候群或其他多毛症中是否有任何角色。
- 若要探索毛髮相關用途，建議優先評估與雄性素有明確關聯的疾病（如雄性素性禿），而非本預測的罕見遺傳性疾病。
- 評估給藥途徑與族群，並建立安全性監測計畫。

<!-- review:begin log -->

## 查核紀錄

以下是本頁的查核紀錄：內容已對照衞生署藥物辦公室的藥劑製品註冊資料。更正只限基本事實，模型預測、證據等級與結論未有改寫。「缺乏作用機轉資料」的句子已改為所列官方仿單的節錄（附非官方翻譯）。

| 查核日期 | 項目 | 處理 | 依據 |
|------|------|------|------|
| 2026-11-19 | 「目前缺乏詳細的作用機轉資料」改為美國處方資料節錄 | 「缺乏作用機轉資料」句改為附出處的仿單節錄 | [DailyMed: dutasteride prescribing information, Strides Pharma Science Limited](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=c78d18cf-05df-4154-b2f9-39cc374ca9e3) |
| 2026-11-24 | 「香港共有 11 張有效許可證（皆為單一成分登記，無已註銷者），列出其中 5 張：」→「香港含本藥成分的許可證包括單一成分與複方製劑（含與 tams」 | 更正 | [衞生署藥物辦公室：藥劑製品註冊名單（DrugList.xml，data.gov.hk；證據包 Release data-20261123-235245）](https://www.drugoffice.gov.hk/eps/psi/DrugList.xml) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

