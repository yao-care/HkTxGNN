---
layout: default
title: Telbivudine
parent: 僅模型預測 (L5)
nav_order: 853
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
description: "Telbivudine：預測新適應症為慢性 C 型肝炎 (Chronic Hepatitis C Virus Infection)（證據等級 L5）。原適應症：慢性 B 型肝炎"
monitor_inn: "TELBIVUDINE"
predicted_indications: ["chronic hepatitis C virus infection", "HIV infectious disease", "hepatitis C virus infection", "disorder of phenylalanine metabolism"]
---

# Telbivudine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Telbivudine：從慢性B型肝炎到慢性C型肝炎

## 一句話總結

Telbivudine 是一種核苷類似物抗病毒藥，原本用於治療慢性 B 型肝炎。
TxGNN 模型預測它可能對**慢性 C 型肝炎 (Chronic Hepatitis C Virus Infection)** 有效，但目前**沒有任何臨床試驗**，現有 **6 篇文獻**也只是 B/C 型肝炎合併討論的綜述或 B 型肝炎研究，不構成直接證據。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 慢性 B 型肝炎（來自知識圖譜；香港許可證未載明適應症文字） |
| 預測新適應症 | 慢性 C 型肝炎 (Chronic Hepatitis C Virus Infection) |
| TxGNN 預測分數 | 99.96% |
| 證據等級 | L5（僅有模型預測，無實際研究支持） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 1 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

Telbivudine 是合成的 L-型胸腺嘧啶核苷類似物，在細胞內被磷酸化後抑制 B 型肝炎病毒 (HBV) 的 DNA 聚合酶（逆轉錄酶），使病毒 DNA 鏈延長終止。目前缺乏更詳細的作用機轉資料。

C 型肝炎病毒 (HCV) 則是靠 RNA 依賴性 RNA 聚合酶 (NS5B) 複製，與 HBV 聚合酶屬於不同的酶類。Telbivudine 對 HCV 的 NS5B 或其他 HCV 標靶沒有已知活性，因此**機轉上找不到支持此預測的依據**。

模型給出 99.96% 的高分，較可能是因為 B 型與 C 型肝炎同屬嗜肝性病毒疾病，在知識圖譜中距離很近，而不是真正的藥理關聯。檢索到的文獻也多是 B/C 型肝炎合併討論的綜述，其中 telbivudine 只用於 B 型肝炎。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [25233195](https://pubmed.ncbi.nlm.nih.gov/25233195/) | 2014 | Review | Journal of Perinatology | 回顧妊娠期 B/C 型肝炎與母嬰傳染的處置建議 |
| [16937041](https://pubmed.ncbi.nlm.nih.gov/16937041/) | 2006 | Review | Wiener Medizinische Wochenschrift | B/C 型肝炎現行治療與展望，B 型肝炎部分討論干擾素與 lamivudine |
| [25027705](https://pubmed.ncbi.nlm.nih.gov/25027705/) | 2014 | Review | Minerva Gastroenterologica e Dietologica | B/C 型肝炎抗病毒藥物對腎功能的影響；telbivudine 列於 B 型肝炎核苷類似物 |
| [18340426](https://pubmed.ncbi.nlm.nih.gov/18340426/) | 2008 | Review | Der Internist | 德國指引：telbivudine 屬 B 型肝炎單一療法選項之一 |
| [21999649](https://pubmed.ncbi.nlm.nih.gov/21999649/) | 2011 | Review | Paediatric Drugs | 兒童慢性肝病的藥物處置，聚焦可治癒或可能治癒的疾病 |
| [23697556](https://pubmed.ncbi.nlm.nih.gov/23697556/) | 2013 | Cohort | J Interferon Cytokine Res | 40 名 B 型肝炎患者接受 telbivudine 治療期間，血清 IL-37 濃度與 HBeAg 血清轉換的關係（僅涉及 B 型肝炎） |

以上文獻都沒有直接顯示 telbivudine 對 C 型肝炎有效。

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-55624 | SEBIVO TAB 600MG（持證商：VIATRIS HEALTHCARE HONG KONG LIMITED） | — | — |

---

## 安全性考量

- **知識圖譜標示的禁忌疾病**（來自藥物與疾病的關聯資料，並非仿單原文）：腎臟疾病、輸尿管積膿、肌病變、肌肉疾病、骨骼肌疾病、家族性週期性麻痺、周邊神經系統疾病、周邊神經病變、脂肪肝、非酒精性脂肪肝炎、乳酸中毒、皮肌炎、肌炎。
- **藥物交互作用**：資料庫共收錄 96 筆，已列出的 20 筆皆為中度。主要包括：
  - 皮質類固醇（hydrocortisone、dexamethasone、prednisone、triamcinolone、betamethasone、budesonide）
  - 兩性黴素 B 類（amphotericin B 及其脂質製劑）
  - 胺基糖苷類與抗生素（kanamycin、neomycin、vancomycin、metronidazole）
  - 水楊酸類腸道消炎藥（mesalazine、sulfasalazine、balsalazide、olsalazine）
  - 他汀類（rosuvastatin、simvastatin）
  - orlistat
- 其他藥典資料指出，此類核苷類似物有肌病變與周邊神經病變風險，與 peginterferon 併用時更需注意。

仿單層級的警語與禁忌資料尚未取得，請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 沒有臨床試驗，文獻也只是 B/C 型肝炎合併討論的綜述，證據等級僅 L5。
- Telbivudine 的標靶是 HBV 聚合酶，對 HCV 沒有已知作用機轉，高預測分數很可能是知識圖譜的類別相近效應。

**補充說明：**
- 同一批預測中，「B 型肝炎」本身（排名第 2）是此藥已核准的適應症，有多項 Phase 3/4 試驗支持（如 NCT00142298，1,869 人）。
- 「HIV 感染」（排名第 3）有研究顯示 telbivudine 對 HIV-1 無抗病毒活性，同樣不建議推進。

**若要推進需要：**
- 體外 HCV 複製子 (replicon) 試驗，確認有無抗 HCV 活性
- 取得詳細的作用機轉資料與香港仿單的警語及禁忌資料
- 確認 telbivudine 在多個市場已退出的背景，以及 C 型肝炎目前已有直接作用抗病毒藥物，評估此方向是否仍有臨床價值
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

