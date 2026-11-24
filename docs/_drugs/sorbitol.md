---
layout: default
title: Sorbitol
parent: 僅模型預測 (L5)
nav_order: 828
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-24
description: "Sorbitol：預測新適應症為運動誘發惡性高熱 (Exercise-induced Malignant Hyperthermia)（證據等級 L5）。原適應症：許可證資料未載明"
monitor_inn: "SORBITOL"
predicted_indications: ["exercise-induced malignant hyperthermia"]
---

# Sorbitol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

## Sorbitol：從（未載明原適應症）到運動誘發惡性高熱
{: .text-alpha }

## 一句話總結

Sorbitol（山梨醣醇）是一種糖醇，常作為滲透性瀉劑、甜味劑與輸液／藥品賦形劑使用，香港許可證資料未載明其核准適應症。
TxGNN 模型預測它可能對**運動誘發惡性高熱 (Exercise-induced Malignant Hyperthermia)** 有效，但目前**沒有任何臨床試驗或文獻**支持這個方向，僅為模型預測。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 許可證資料未載明 |
| 預測新適應症 | 運動誘發惡性高熱 (Exercise-induced Malignant Hyperthermia) |
| TxGNN 預測分數 | 0.9940 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 11 張／共 11 張） |
| 許可證數 | 11 張（有效 11 張） |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料，香港許可證也未列出原適應症。已知 Sorbitol 是糖醇類化合物，用於滲透性瀉劑、甜味劑與賦形劑。

惡性高熱是一種藥物基因體疾病，與骨骼肌鈣離子調控異常有關（常見 RYR1 或 CACNA1S 變異），多由揮發性麻醉劑或琥珀膽鹼誘發。運動誘發的熱相關疾病與其相關，但並不相同。Sorbitol 對 ryanodine 受體功能、細胞內鈣離子釋放或肌肉產熱沒有已知作用，現有資料也找不到兩者的機轉連結。標準治療藥物 dantrolene 是 RyR1 拮抗劑，與 Sorbitol 的作用方式無關。

0.9940 的高分是 TxGNN 模型（深度學習）給出的預測分數，可能反映模型學到的相關疾病之間的相似性，不代表有生物學依據。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

---

## 香港上市資訊

香港含本藥成分的許可證皆為複方（張數與有效張數見本頁快速總覽與「香港上市資訊」的許可證表）。核准適應症與劑型欄位在許可證資料中皆為空白。以下列出 5 張主要許可證：

<!-- review:begin hk-lic-20261124b-sorbitol-1 -->

> **查核更正（2026-11-24）**：原文為「香港共有 11 張有效許可證（皆為單方，無已註銷者）。」。已更正：依衞生署藥物辦公室註冊名單的成分欄，含本藥成分的許可證皆為複方；原句的單一成分／複方說法或張數跟註冊名單不符（舊報告依證據包以「;;」切成分，每張都算成單方）。張數見本頁快速總覽與許可證表（2026-11-24 核對）。依據：[衞生署藥物辦公室：藥劑製品註冊名單（DrugList.xml，data.gov.hk；證據包 Release data-20261123-235245）](https://www.drugoffice.gov.hk/eps/psi/DrugList.xml)。

<!-- review:end hk-lic-20261124b-sorbitol-1 -->

<!-- licenses:begin -->

| 許可證號 | 品名 | 類別 | 持證商 | 狀態 |
|------|------|------|------|------|
| HK-28237 | OSMOFUNDIN IV INFUSION 20% | 複方 | B. BRAUN MEDICAL (HK) LTD | 有效 |
| HK-62100 | AMINOGEN-S SOLUTION FOR INFUSION | 複方 | WINGS PHARMACEUTICAL LTD | 有效 |
| HK-57540 | AMINOL-S INJ | 複方 | WINGS PHARMACEUTICAL LTD | 有效 |
| HK-55215 | PAN-AMIN G INJ | 複方 | OTSUKA PHARMACEUTICAL (H.K.) LIMITED | 有效 |
| HK-59756 | CELAMIN G INJ | 複方 | FALKAN MEDICAL LIMITED | 有效 |

上表列出其中 5 張（共 11 張）。

<!-- licenses:end -->

---

## 安全性考量

- **知識圖譜標示的禁忌疾病**：活動性消化性潰瘍（來自藥物—疾病知識圖譜的禁忌關聯，並非仿單文字）。
- **藥物交互作用**（共 2 筆）：
  - Tolevamer：**Major**（嚴重）
  - Lamivudine：Moderate（中度）

其他警語與禁忌症請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 證據等級為 L5，僅有模型預測，沒有臨床試驗、文獻或機轉依據；Sorbitol 與惡性高熱的病理機轉（鈣離子調控異常）之間沒有可辨識的連結。
- 惡性高熱已有明確的標準治療（dantrolene），且 Sorbitol 有已知的消化性潰瘍禁忌與一項嚴重交互作用。

**若要推進需要：**
- 補齊 Sorbitol 的作用機轉資料，並釐清香港許可證的實際核准適應症與劑型。
- 取得香港衛生署仿單的警語與禁忌症。
- 以文獻回顧或前臨床實驗（如肌肉細胞鈣離子釋放模型）驗證是否存在任何生物學關聯。
- 確認 TxGNN 模型（深度學習）的高分是否只反映模型學到的相關疾病之間的相似性，再決定是否重新評估。

<!-- review:begin log -->

## 查核紀錄

以下是本頁的查核紀錄：內容已對照衞生署藥物辦公室的藥劑製品註冊資料。更正只限基本事實，模型預測、證據等級與結論未有改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|------|------|------|------|
| 2026-11-24 | 「香港共有 11 張有效許可證（皆為單方，無已註銷者）。」→「香港含本藥成分的許可證皆為複方（張數與有效張數見」 | 更正 | [衞生署藥物辦公室：藥劑製品註冊名單（DrugList.xml，data.gov.hk；證據包 Release data-20261123-235245）](https://www.drugoffice.gov.hk/eps/psi/DrugList.xml) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

