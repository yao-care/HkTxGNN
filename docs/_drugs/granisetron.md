---
layout: default
title: Granisetron
parent: 僅模型預測 (L5)
nav_order: 427
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
description: "Granisetron：預測新適應症為躁期雙極性情感疾患 (Manic Bipolar Affective Disorder)（證據等級 L5）。原適應症：本次整理的資料中，許可證未載明核准適應症"
monitor_inn: "GRANISETRON"
predicted_indications: ["manic bipolar affective disorder", "Tourette syndrome", "acute contagious conjunctivitis", "angioedema", "allergic urticaria"]
---

# Granisetron
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

## Granisetron：從化療引起的噁心嘔吐到躁期雙極性情感疾患
{: .text-alpha }

## 一句話總結

Granisetron 是選擇性 5-HT3 受體拮抗劑，在香港已有多張許可證，屬於止吐類藥物。
TxGNN 模型預測它可能對**躁期雙極性情感疾患 (Manic Bipolar Affective Disorder)** 有效，
但目前**沒有任何臨床試驗或文獻**支持，僅有模型預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 本次整理的資料中，許可證未載明核准適應症 |
| 預測新適應症 | 躁期雙極性情感疾患 (Manic Bipolar Affective Disorder) |
| TxGNN 預測分數 | 99.62% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 11 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。已知 Granisetron 是選擇性 5-HT3 受體拮抗劑。有假說認為，調節 5-HT3 可能影響與情緒調節相關的多巴胺與血清素訊號。

不過，這只是理論上的推測。資料中沒有任何臨床試驗或文獻佐證，0.996 的高分只是計算模型的預測結果，不能視為療效證據。

**其他預測適應症（同樣僅有模型預測，皆為 L5、建議 Hold）：**

| 排名 | 預測適應症 | TxGNN 分數 | 機轉合理性簡述 |
|------|-----------|-----------|----------------|
| 2 | 妥瑞氏症 (Tourette syndrome) | 99.52% | 5-HT3 拮抗可能調節基底核多巴胺迴路；其他同類藥物（如 ondansetron）有小型研究，但 granisetron 無資料 |
| 3 | 急性傳染性結膜炎 | 99.49% | 5-HT3 拮抗與病毒或細菌感染的病因之間沒有明顯機轉關聯，高分可能是網路關聯的假象 |
| 4 | 血管性水腫 (Angioedema) | 99.36% | 血清素可能參與神經源性發炎與血管通透性，屬推測性連結，尚未證實 |
| 5 | 過敏性蕁麻疹 | 99.32% | 肥大細胞釋放血清素及 5-HT3 相關搔癢訊號有推測性依據，但無 granisetron 的臨床資料 |

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

香港共有 11 張有效單方許可證，無已註銷者。本次整理的資料中，各許可證的劑型與核准適應症均未載明，以下列出 5 張主要許可證：

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-36669 | KYTRIL FOR IV INFUSION 0.1% | PRUDENTLINK LIMITED |
| HK-61365 | KYTRIL FILM-COATED TABLETS 1MG | PRUDENTLINK LIMITED |
| HK-44569 | KYTRIL INJ 1MG/ML AMPOULE | PRUDENTLINK LIMITED |
| HK-60565 | GRANISETRON KABI CONCENTRATE FOR SOLUTION FOR INJ OR INF 1MG/1ML | FRESENIUS KABI HONG KONG LIMITED |
| HK-60439 | GRANISETRON ACTAVIS TAB 1MG | TEVA PHARMACEUTICAL HONG KONG |

從品名可見，產品包含口服錠劑與注射/輸注劑型。

## 安全性考量

- **知識圖譜標示的禁忌疾病**（來自藥物與疾病的關聯資料，並非仿單文字）：long QT syndrome（長 QT 症候群）、familial long QT syndrome（家族性長 QT 症候群）、potassium deficiency disease（缺鉀症）、sudden cardiac arrest（心因性猝死）、heart conduction disease（心臟傳導疾病）。整體指向 QT 間期延長與心律不整風險。
- **藥物交互作用**：共查得 100 筆，以下為其中部分。
  - **嚴重 (Major)**：Fentanyl、Alfentanil、Tramadol、Dextromethorphan、Almotriptan、Sumatriptan、Amiodarone、Amisulpride、Amitriptyline、Anagrelide。這些多與 QT 延長或血清素症候群風險相關。
  - **中度 (Moderate)**：Abametapir、Abiraterone、Dihydrocodeine、Codeine、Famotidine、Formoterol、Adenosine、Salbutamol、Alfuzosin、Propofol。

其他警語與禁忌請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 所有預測適應症都僅有 TxGNN 模型分數，沒有臨床試驗或文獻（證據等級 L5）。
- 作用機轉資料不足，且與心律相關的禁忌與多項嚴重藥物交互作用，使躁期雙極性情感疾患患者（常併用精神科藥物）的風險更需謹慎評估。

**若要推進需要：**
- 補充 DrugBank 的作用機轉資料，並取得香港衛生署仿單的警語與禁忌。
- 系統性搜尋 granisetron 與 5-HT3 拮抗劑用於雙極性疾患（及妥瑞氏症）的臨床前與臨床研究。
- 釐清與常用情緒穩定劑、抗精神病藥併用時的 QT 延長風險。
- 若文獻支持，再規劃小型探索性試驗，並納入心電圖與電解質監測。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

