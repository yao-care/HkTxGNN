---
layout: default
title: Telbivudine
parent: 僅模型預測 (L5)
nav_order: 853
evidence_level: L5
indication_count: 9
monitor_inn: "TELBIVUDINE"
predicted_indications: ["chronic hepatitis C virus infection", "HIV infectious disease", "hepatitis C virus infection", "disorder of phenylalanine metabolism", "disorder of tyrosine metabolism", "feline acquired immunodeficiency syndrome", "simian immunodeficiency virus infection", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter", "tetrahydrobiopterin-responsive hyperphenylalaninemia/phenylketonuria"]
last_modified_at: 2026-10-23
description: "Telbivudine：預測新適應症為慢性 C 型肝炎病毒感染 (chronic hepatitis C virus infection)（證據等級 L5）。原適應症：本地許可證資料未記載適應症"
---

# Telbivudine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

## Telbivudine: 慢性 C 型肝炎病毒感染 (chronic hepatitis C virus infection)
{: .text-alpha }

## 一句話總結

Telbivudine 是一種核苷類似物抗病毒藥，知識圖譜記錄的原適應症為慢性 B 型肝炎病毒感染。
TxGNN 模型預測它可能對**慢性 C 型肝炎病毒感染 (Chronic Hepatitis C Virus Infection)** 有效，但目前**沒有臨床試驗**，僅有 6 篇文獻，且都未直接顯示它對 C 型肝炎病毒有活性，因此證據極弱。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 本地許可證資料未記載適應症 |
| 預測新適應症 | 慢性 C 型肝炎病毒感染 (chronic hepatitis C virus infection) |
| TxGNN 預測分數 | 0.9996 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 1 張／共 1 張） |
| 許可證數 | 1 張（有效 1 張） |
| 核准張數 | 1 張（單一成分） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。就已知資訊，telbivudine 是胸腺嘧啶核苷類似物，可抑制 B 型肝炎病毒 (HBV) 的 DNA 聚合酶（反轉錄酶）。

C 型肝炎病毒 (HCV) 靠 RNA 依賴性 RNA 聚合酶 (NS5B) 複製，telbivudine 並無已知的抑制作用。模型的高分很可能反映兩種病毒同屬「病毒性肝炎」的網路鄰近關係，而不是真正的機轉關聯。

因此，這個預測的分數來自 TxGNN 模型（深度學習），可能反映模型學到的相關疾病之間的相似性，而非生物學證據。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

下列文獻皆為綜述或相關研究，沒有一篇顯示 telbivudine 對 HCV 有活性。

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [25233195](https://pubmed.ncbi.nlm.nih.gov/25233195/) | 2014 | Review | J Perinatol | 回顧妊娠合併 B 型與 C 型肝炎及母嬰傳染的預防 |
| [16937041](https://pubmed.ncbi.nlm.nih.gov/16937041/) | 2006 | Review | Wien Med Wochenschr | 慢性 B 型與 C 型肝炎的現行治療與未來展望 |
| [25027705](https://pubmed.ncbi.nlm.nih.gov/25027705/) | 2014 | Review | Minerva Gastroenterol Dietol | B 型與 C 型肝炎抗病毒藥物對腎功能的影響 |
| [18340426](https://pubmed.ncbi.nlm.nih.gov/18340426/) | 2008 | Review | Der Internist | B 型與 C 型肝炎抗病毒治療的新資料與建議 |
| [21999649](https://pubmed.ncbi.nlm.nih.gov/21999649/) | 2011 | Review | Paediatr Drugs | 兒童慢性肝病的內科處置 |
| [23697556](https://pubmed.ncbi.nlm.nih.gov/23697556/) | 2013 | Cohort | J Interferon Cytokine Res | 慢性 B 型肝炎患者接受 telbivudine 治療期間，血清 IL-37 與 HBeAg 血清轉換的關係（研究對象為 HBV，非 HCV） |

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-55624 | SEBIVO TAB 600MG | 未載明 | 未載明 |

## 安全性考量

- **知識圖譜記錄的禁忌關聯（非仿單內容）**：腎臟疾病、肌病／肌肉疾病、骨骼肌疾病、家族性週期性麻痺、周邊神經系統疾病、周邊神經病變、脂肪肝、非酒精性脂肪肝炎、乳酸酸中毒、皮肌炎、肌炎，以及膿輸尿管。
- **藥物交互作用**：共查得 96 筆，以下為部分中度交互作用：
  - 類固醇：hydrocortisone、dexamethasone、prednisone 等
  - 抗微生物藥：amphotericin B、vancomycin、neomycin、metronidazole 等
  - 其他：mesalazine、sulfasalazine、rosuvastatin、simvastatin、orlistat 等

本次未取得香港仿單的警語與禁忌文字，詳細安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 沒有直接研究 C 型肝炎的臨床試驗或文獻，機轉上也無合理依據（telbivudine 作用於 HBV 聚合酶，而非 HCV 的 NS5B），證據等級僅為 L5。
- 高預測分數很可能來自病毒性肝炎的共現關聯，不足以支持推進。

**若要推進需要：**
- 取得 telbivudine 對 HCV 複製的體外活性（如 replicon 試驗）資料
- 補充作用機轉資料
- 取得香港仿單的警語與禁忌資訊，並評估肌病、周邊神經病變及乳酸酸中毒等風險
- 若體外試驗沒有活性，建議停止此方向

## 其他預測適應症的簡要說明

其他排名靠前的預測同樣缺乏支持，均維持 L5 與 Hold：

- **HIV 感染**：有一項試驗登記（NCT00051090），但已撤回、入組 0 人，且評估的是 HBV／HIV 共感染中的抗 HBV 治療。PMID 22024528 與 PMID 20308377 顯示 telbivudine 對 HIV-1 無抗病毒活性。
- **C 型肝炎病毒感染（另一條目）**：文獻多為 B 型與 C 型肝炎合併討論的綜述，無 telbivudine 抗 HCV 的證據。
- **苯丙胺酸／酪胺酸代謝異常、四氫生物蝶呤反應性高苯丙胺酸血症／苯酮尿症、罕見神經發育疾病、貓免疫缺乏症候群、猿猴免疫缺乏病毒感染**：無試驗與文獻，也無機轉依據，分數來自 TxGNN 模型（深度學習），很可能只是反映模型學到的相關疾病之間的相似性，而非生物學證據。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

