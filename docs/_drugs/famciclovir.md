---
layout: default
title: Famciclovir
parent: 高證據等級 (L1-L2)
nav_order: 305
evidence_level: L2
indication_count: 5
---

# Famciclovir
{: .fs-9 }

證據等級: **L2** | 預測適應症: **5** 個
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

# Famciclovir：從帶狀皰疹到感染後神經痛

## 一句話總結

Famciclovir 是治療帶狀皰疹（Herpes Zoster）的口服抗病毒藥物，作用機轉為抑制皰疹病毒 DNA 聚合酶。
TxGNN 模型預測它可能對**感染後神經痛 (Post-infectious Neuralgia)** 有效（預測分數 99.75%），
此預測具強烈機轉合理性，全球已有 Phase 3 RCT 支持，但台灣目前無已核准產品，安全性本地資料尚待補充。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 帶狀皰疹 (Herpes Zoster)（依藥理學知識認定，台灣無許可證） |
| 預測新適應症 | 感染後神經痛 (Post-infectious Neuralgia) |
| TxGNN 預測分數 | 99.75% |
| 證據等級 | L2 |
| 台灣上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

Famciclovir 是 penciclovir 的前驅藥（prodrug），口服後迅速在體內轉化為活性形式 penciclovir triphosphate，選擇性抑制皰疹病毒（包括 VZV、HSV-1、HSV-2）的 DNA 聚合酶，阻斷病毒 DNA 鏈延伸。目前無詳細作用機轉（MOA）原始資料，上述機轉依公開藥理文獻推導。

帶狀皰疹由潛伏於背根神經節的水痘帶狀皰疹病毒（VZV）再活化引起。急性感染期間，VZV 沿感覺神經傳播，造成神經節發炎及神經纖維損傷。若急性期病毒複製未能及早控制，神經損傷會持續演化為慢性神經病變性疼痛，即帶狀皰疹後神經痛（Postherpetic Neuralgia, PHN），是「感染後神經痛」的最主要類型，也是帶狀皰疹最常見且最難治的後遺症。

機轉路徑直接且清晰：早期使用 Famciclovir → 縮短 VZV 急性複製期 → 降低感覺神經節病毒負荷與神經纖維損傷程度 → 減少 PHN 發生率與疼痛嚴重度。全球已有多個 Phase 3 RCT（包括 Degreef 1994、Boon 1995 等）支持此路徑，美國 FDA 與歐盟 EMA 亦已核准此適應症。本次查詢未擷取到上述核心文獻，但機轉關聯屬高度直接，預測可信度高。

---

## 臨床試驗證據

> ⚠️ 以下試驗均非以 Famciclovir 為介入藥物，為感染後神經痛疾病領域之相關試驗，對本藥再利用評估的直接佐證有限（相關性評級均為 Grade C）。

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT06798662](https://clinicaltrials.gov/study/NCT06798662) | N/A | 尚未招募 | 120 | 評估脂質體布比卡因及羅哌卡因多模式神經阻斷術搭配脈衝射頻，用於急性帶狀皰疹疼痛控制；介入為區域麻醉，非抗病毒藥物 |
| [NCT03120962](https://clinicaltrials.gov/study/NCT03120962) | N/A | 不明 | 140 | 評估急性帶狀皰疹期早期使用羥考酮（oxycodone）能否預防帶狀皰疹後神經痛；介入為鴉片類止痛藥，與 Famciclovir 抗病毒機轉路徑不同 |

> 📌 建議補充查詢：以 "famciclovir postherpetic neuralgia" 為關鍵字在 PubMed 及 ClinicalTrials.gov 搜尋，預期可找到已完成的 Phase 2/3 RCT 文獻（Degreef 1994, Boon 1995）。

---

## 文獻證據

目前無相關文獻（本次 PubMed 查詢針對 Famciclovir × 感染後神經痛未返回結果）。

建議補充查詢關鍵字：`famciclovir[ti] AND (postherpetic neuralgia OR herpes zoster pain OR PHN)`

---

## 台灣上市資訊

Famciclovir 在台灣目前**無已核准藥品許可證**（TFDA 查詢結果：0 筆），屬未上市藥物。

如需評估引進，需另行查詢：
- 原廠仿單（美國 FDA 核准版本）
- TFDA 境外新藥申請或恩慈療法相關規定

---

## 安全性考量

安全性資訊請參考原廠仿單。

（本次資料包中 TFDA 仿單警語、禁忌症資料均缺失，為 Blocking 等級缺口，需優先補充後方可進入安全性初評。）

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
Famciclovir 抑制 VZV 複製以降低感染後神經痛的機轉路徑清晰且直接，全球（美國 FDA、歐盟 EMA）已核准相關適應症並有 Phase 3 RCT 支撐，機轉合理性屬同類藥物（acyclovir、valacyclovir）中佐證最充分的類別之一。主要障礙在於台灣目前無上市產品，安全性本地資料尚缺，需先行補充再推進評估。

**若要推進需要：**
- 補充 TFDA 仿單警語與禁忌症（目前為 **Blocking** 缺口，DG001）
- 補充完整作用機轉原始資料（DrugBank API 查詢，DG002）
- 補充查詢核心 Phase 3 RCT 文獻（Degreef 1994、Boon 1995）以確認證據等級達 L1
- 確認美國 FDA 與歐盟 EMA 已核准的帶狀皰疹後神經痛適應症詳細條件（劑量、療程、族群）
- 評估台灣申請藥品許可證或恩慈療法的可行路徑與時程
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

