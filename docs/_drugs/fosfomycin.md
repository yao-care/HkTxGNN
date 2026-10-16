---
layout: default
title: Fosfomycin
parent: 高證據等級 (L1-L2)
nav_order: 401
evidence_level: L2
indication_count: 5
last_modified_at: 2026-10-14
description: "Fosfomycin：預測新適應症為淋病性尿道炎 (Gonococcal Urethritis)（證據等級 L2）。原適應症：泌尿道感染"
---

# Fosfomycin
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

# Fosfomycin：從泌尿道感染到淋病性尿道炎

## 一句話總結

Fosfomycin（磷黴素）是一種抗生素，原本用於治療泌尿道感染。
TxGNN 模型預測它可能對**淋病性尿道炎 (Gonococcal Urethritis)** 有效，
目前有 **1 篇隨機對照試驗**和另外數篇相關文獻支持這個方向，但尚無已登記的臨床試驗。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 泌尿道感染（許可證未載明適應症文字，此為知識圖譜資料） |
| 預測新適應症 | 淋病性尿道炎 (Gonococcal Urethritis) |
| TxGNN 預測分數 | 99.99% |
| 證據等級 | L2 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 1 張 |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（原始 MOA 欄位為空白）。以下說明是依據對此藥物的一般認識，而非本次整理的資料記錄：Fosfomycin 抑制 MurA 酶（UDP-N-acetylglucosamine enolpyruvyl transferase），阻斷肽聚醣（peptidoglycan）合成的第一步，屬於殺菌性機轉，理論上對淋病奈瑟菌 (*Neisseria gonorrhoeae*) 有活性。

泌尿道感染與尿道炎在解剖位置上相近，而 fosfomycin 在尿液中可達高濃度，這是它用於泌尿道感染的基礎，也支持其用於尿道感染的合理性。

值得注意的是，一項 2016 年的隨機對照試驗直接測試了 fosfomycin trometamol 對單純性淋病性尿道炎的療效，使這個預測比單純的模型推論更有依據。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [27064136](https://pubmed.ncbi.nlm.nih.gov/27064136/) | 2016 | RCT | Clin Microbiol Infect | 152 名男性的開放性隨機對照試驗，126 人完成；fosfomycin trometamol 3 g 口服（第 1、3、5 天）用於單純性淋病性尿道炎 |
| [832528](https://pubmed.ncbi.nlm.nih.gov/832528/) | 1977 | 臨床研究 | Chemotherapy | 70 名急性或亞急性淋病性尿道炎患者接受肌肉注射；4 g 總劑量組 11/12 治癒（92%），單次 4 g 組 37/43 治癒（86%） |
| [832523](https://pubmed.ncbi.nlm.nih.gov/832523/) | 1977 | 臨床細菌學評估 | Chemotherapy | 西班牙多家醫院 959 名患者的對照臨床研究，涵蓋淋病性尿道炎等多種感染，評估 fosfomycin 的廣譜抗菌表現 |
| [19593988](https://pubmed.ncbi.nlm.nih.gov/19593988/) | 2009 | 回顧／臨床文章 | Zhonghua Nan Ke Xue | 探討非淋病性奈瑟菌對男性泌尿生殖道感染診斷與治療的影響（與 fosfomycin 關聯有限） |
| [35820778](https://pubmed.ncbi.nlm.nih.gov/35820778/) | 2023 | 次級分析 | Sex Transm Infect | NABOGO 試驗中無症狀淋病的自發清除分析（非 fosfomycin 專屬） |
| [17878816](https://pubmed.ncbi.nlm.nih.gov/17878816/) | 2007 | 個案報告 | J Fr Ophtalmol | 成人淋病性結膜炎併發角膜穿孔個案（相關性低） |

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-43159 | MONUROL SACHETS 3G | 未載明 | 未載明 |

---

## 安全性考量

- **知識圖譜標示之相關疾病禁忌**（非仿單內容）：腎臟疾病、輸尿管積膿 (pyoureter)、困難梭菌結腸炎 (*Clostridium difficile* colitis)、周產期壞死性腸炎
- **藥物交互作用**（共 3 項）：
  - Balsalazide：中度
  - Picosulfuric acid：中度
  - Metoclopramide：輕度

其他警語與禁忌請參考原廠仿單。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 已有一項 2016 年的隨機對照試驗直接針對淋病性尿道炎，另有 1977 年的臨床研究提供治癒率資料，證據等級為 L2。但該 RCT 為開放性試驗，且目前無已登記的臨床試驗。
- 淋病奈瑟菌的抗藥性情形與現行治療指引已有變化，需以近期資料重新評估。

**若要推進需要：**
- 取得香港原廠仿單，確認警語、禁忌與核准適應症
- 補充詳細的作用機轉資料（MOA）
- 取得 2016 年 RCT 的完整結果，包括治癒率與比較組
- 評估當前本地淋病奈瑟菌對 fosfomycin 的敏感性與現行治療指引
- 針對腎功能不全患者及知識圖譜所列禁忌疾病，制定使用限制與監測方案

---

### 其他預測適應症備註

其餘預測的證據都明顯較弱，建議暫緩（Hold）：
- **Ureaplasma 尿道炎**：僅有模型預測。Ureaplasma 沒有細胞壁，作用於細胞壁合成的 fosfomycin 在機轉上不合理，可能是圖譜推論的假象。
- **子宮發炎性疾病**：僅有 2 個一般性兒童藥物動力學研究，與此適應症無直接關聯。
- **黃色肉芽腫性腎盂腎炎**：僅有間接的機轉合理性，通常需要手術處理，單用抗生素多半無法治癒。
- **會厭炎**：屬呼吸道急症，已有標準靜脈抗生素治療，無支持 fosfomycin 的臨床依據。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

