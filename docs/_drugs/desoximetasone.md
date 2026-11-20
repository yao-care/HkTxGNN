---
layout: default
title: Desoximetasone
parent: 高證據等級 (L1-L2)
nav_order: 262
evidence_level: L2
indication_count: 10
last_modified_at: 2026-11-20
monitor_inn: "DESOXIMETASONE"
predicted_indications: ["alopecia areata", "alopecia mucinosa", "telogen effluvium", "hereditary hypotrichosis with recurrent skin vesicles", "Quinquaud's folliculitis decalvans", "alopecia antibody deficiency", "alopecia-intellectual disability-hypergonadotropic hypogonadism syndrome", "primary cutaneous B-cell lymphoma", "atrichia with papular lesions", "vulvar inverted follicular keratosis"]
description: "Desoximetasone：預測新適應症為圓形禿 (alopecia areata)（證據等級 L2）。香港藥劑製品註冊：1 張（有效 1 張）"
---

# Desoximetasone
{: .fs-9 }

證據等級: **L2** | 預測適應症: **10** 個
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

## Desoximetasone: 圓形禿 (alopecia areata)
{: .text-alpha }

## 一句話總結

Desoximetasone 是一種強效局部皮質類固醇，具有抗發炎與免疫抑制作用。
TxGNN 模型預測它可能對**圓形禿 (alopecia areata)** 有效，
目前有 **1 篇隨機雙盲安慰劑對照試驗**（以 0.25% desoximetasone 乳膏治療圓形禿）支持這個方向，證據等級為 **L2**，尚無已登記的臨床試驗。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 本地許可證資料未記載適應症 |
| 預測新適應症 | 圓形禿 (alopecia areata) |
| TxGNN 預測分數 | 0.9992 |
| 證據等級 | L2 |
| 香港上市 | 上市中（有效許可證 1 張／共 1 張） |
| 許可證數 | 1 張（有效 1 張） |
| 建議決策 | Proceed with Guardrails |

## 為什麼這個預測合理？

圓形禿是一種由 T 細胞介導的自體免疫疾病，免疫細胞攻擊毛囊。Desoximetasone 是強效局部皮質類固醇，能抑制毛囊周圍的免疫細胞浸潤與發炎反應，機轉上具合理性。

上述推論主要依據皮質類固醇類別的已知藥理：藉由糖皮質素受體 (NR3C1) 發揮抗發炎與免疫調節作用。根據美國 FDA 核准的 Desoximetasone 處方資料（Prescribing Information）「Mechanism of Action」段（非官方翻譯）：「皮質類固醇在細胞訊息傳遞、免疫功能、發炎及蛋白質調節中扮演一定角色；然而，其在乾癬中的確切作用機制尚不明確。」英文原文："Corticosteroids play a role in cellular signaling, immune function, inflammation and protein regulation; however, the precise mechanism of action in psoriasis is unknown."（[DailyMed: Topicort (desoximetasone) prescribing information, Sun Pharmaceutical Industries, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=e417856a-b760-4626-bc34-8e4bc62c026c)，版本日期 2025-07-02；查閱日期 2026-11-19）。局部皮質類固醇在臨床上也已被用於圓形禿的處置。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [11030789](https://pubmed.ncbi.nlm.nih.gov/11030789/) | 2000 | RCT | Archives of Dermatology | 隨機、雙盲、安慰劑對照試驗，評估 0.25% desoximetasone 乳膏治療圓形禿（本資料未提供摘要，無法摘要具體療效數據） |

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-59501 | INERSON OINTMENT 0.25% | 軟膏（依品名判斷） | 許可證資料未載明 |

## 安全性考量

- **藥物交互作用**：藥理資料顯示 desoximetasone 作用於糖皮質素受體 (NR3C1)；未提供具臨床分級的藥物間交互作用。

其餘警語與禁忌症資料請參考原廠仿單。

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
已有 1 篇針對圓形禿、使用 0.25% desoximetasone 乳膏的隨機雙盲安慰劑對照試驗，且機轉上合理，因此證據等級為 L2。但該試驗發表於 2000 年，缺乏摘要層級的療效數據，也沒有登記中的臨床試驗，需審慎推進。

**若要推進需要：**
- 取得 PMID 11030789 全文，確認療效指標、毛髮再生幅度與安全性結果
- 補充 desoximetasone 的作用機轉資料（MOA）
- 取得香港仿單的警語與禁忌症，並確認可用劑型與使用部位（頭皮）
- 進一步的確證性試驗，並規劃長期使用的皮膚萎縮與全身吸收監測

<!-- review:begin log -->

## 查核紀錄

以下是本頁的查核紀錄。「缺乏作用機轉資料」的句子已改為所列官方仿單的節錄（附非官方翻譯）；模型預測、證據等級與結論都沒有改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|------|------|------|------|
| 2026-11-20 | "目前缺乏詳細的作用機轉資料（MOA 欄位為資料缺口）。上述推論主要依據皮質類固醇類別的已知藥理：藉由糖皮質素受體 (NR3C1) 發揮抗發炎與免疫調節作用。" replaced with a sourced mechanism-of-action statement | 「缺乏作用機轉資料」句改為附出處的仿單節錄（2026-11-20 修訂，前版保留於紀錄） | [DailyMed: Topicort (desoximetasone) prescribing information, Sun Pharmaceutical Industries, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=e417856a-b760-4626-bc34-8e4bc62c026c) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

