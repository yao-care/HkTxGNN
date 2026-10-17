---
layout: default
title: Indomethacin
parent: 僅模型預測 (L5)
nav_order: 468
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
description: "Indomethacin：預測新適應症為短指併指症候群 (Brachydactyly-Syndactyly Syndrome)（證據等級 L5）。原適應症：滑囊炎、滑膜炎、類風濕性關節炎、僵直性脊椎炎、痛風、骨關節炎、五十肩、動脈導管未閉等"
monitor_inn: "INDOMETHACIN"
predicted_indications: ["brachydactyly-syndactyly syndrome", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "acromesomelic dysplasia, Hunter-Thompson type", "WHIM syndrome", "brachyolmia-amelogenesis imperfecta syndrome"]
---

# Indomethacin
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

# Indomethacin：從關節炎與發炎性疾病到 Brachydactyly-Syndactyly 症候群

## 一句話總結

Indomethacin 是一種非類固醇消炎藥，原本用於治療滑囊炎、類風濕性關節炎、僵直性脊椎炎、痛風、骨關節炎及早產兒動脈導管未閉等疾病。
TxGNN 模型預測它可能對**短指併指症候群 (Brachydactyly-Syndactyly Syndrome)** 有效，但目前**沒有任何臨床試驗或文獻**支持，僅屬模型預測。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 滑囊炎、滑膜炎、類風濕性關節炎、僵直性脊椎炎、痛風、骨關節炎、五十肩、動脈導管未閉等 |
| 預測新適應症 | 短指併指症候群 (Brachydactyly-Syndactyly Syndrome) |
| TxGNN 預測分數 | 99.97% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 20 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。Indomethacin 一般被認為是非選擇性 COX 抑制劑（此為背景知識，並非來自本報告彙整的資料），透過減少前列腺素合成發揮消炎與止痛作用，因此適用於各類發炎性關節與軟組織疾病。

短指併指症候群屬於先天性肢體發育異常，成因多為基因或發育路徑缺陷，而非發炎。以消炎為主的 COX 抑制作用，並無明確理由能矯正這類發育性病理。因此，就現有資料而言，**找不到可支持此預測的機轉連結**。

99.97% 的高分僅代表模型的計算結果，沒有任何臨床試驗或文獻佐證，不能視為療效證據。其他排名前五的預測（如 colobomatous microphthalmia-rhizomelic dysplasia syndrome、acromesomelic dysplasia Hunter-Thompson type、WHIM syndrome、brachyolmia-amelogenesis imperfecta syndrome）同樣缺乏證據，也沒有合理的機轉連結。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

---

## 香港上市資訊

香港共有 20 張有效的單一成分許可證，以下列出 5 張主要許可證（資料中未提供劑型與核准適應症文字）：

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-01934 | INDOCID CAP 25MG | 膠囊 | 未提供 |
| HK-46461 | RHEUMAXIN CAP 50MG | 膠囊 | 未提供 |
| HK-67282 | TOSPAN INDOMETHACIN CAPSULES 25MG | 膠囊 | 未提供 |
| HK-27094 | INDYLON CAP 25MG | 膠囊 | 未提供 |
| HK-62726 | INDECIN CREAM 1% W/W | 乳膏（外用） | 未提供 |

---

## 安全性考量

- **知識圖譜標示的禁忌疾病**（來自 TxGNN 知識圖譜的藥物-疾病關聯，非仿單內容）：
  - 心血管：高血壓、心肌梗塞、冠狀動脈血栓、心臟病
  - 消化道：胃潰瘍、十二指腸潰瘍、活動性消化性潰瘍、潰瘍性結腸炎、發炎性腸道疾病、壞死性腸炎、食道運動異常
  - 腎臟與肝膽：腎臟疾病、肝臟疾病、膽囊疾病
  - 血液與出血：血小板低下、凝血異常、顱內出血、血紅素病變
  - 呼吸道：氣喘（內因性、過敏性）
  - 神經精神：癲癇、焦慮症、精神官能症、輕鬱症
  - 其他：感染性疾病、輸尿管積膿
- **藥物交互作用**：資料庫共查得 100 筆，以下為其中的主要項目。
  - 中度：阿斯匹靈 (Acetylsalicylic acid)、皮質類固醇（Hydrocortisone、Dexamethasone、Betamethasone、Budesonide、Triamcinolone）、Metformin、Glimepiride、Chlorpropamide、Mesalazine、Balsalazide、Aprepitant、鉀鹽類（Potassium citrate、Potassium bicarbonate）
  - 輕微：Famotidine、Ranitidine、Cimetidine、Linaclotide

仿單的警語與禁忌症資料尚未取得，詳細安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 此預測只有模型分數，沒有任何臨床試驗或文獻，證據等級為 L5。
- 目標疾病是先天發育性異常，與 COX 抑制的消炎作用之間缺乏合理的機轉連結。

**若要推進需要：**
- 補齊 Indomethacin 的作用機轉資料，並重新評估與目標疾病的機轉關聯
- 取得香港衛生署仿單的警語與禁忌症
- 進行文獻與臨床試驗檢索，確認是否有任何支持性證據
- 若仍要探索，需先有前臨床或疾病模型研究，再評估風險與效益
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

