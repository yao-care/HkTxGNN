---
layout: default
title: Dasatinib
parent: 僅模型預測 (L5)
nav_order: 243
evidence_level: L5
indication_count: 10
---

# Dasatinib
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Dasatinib：從慢性骨髓性白血病到尤文氏肉瘤

## 一句話總結

Dasatinib 是口服多標靶激酶抑制劑，依文獻記載原本用於慢性骨髓性白血病 (CML) 與 Ph 陽性急性淋巴性白血病。
TxGNN 模型預測它可能對**尤文氏肉瘤 (Ewing sarcoma)** 有效，但支持的證據偏弱：**3 個臨床試驗**（僅 2 個實際使用 dasatinib）、**9 篇文獻**，且多為前臨床研究。
唯一相關的 Phase 2 肉瘤試驗顯示，dasatinib 單藥在尤文氏肉瘤效果有限。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 慢性骨髓性白血病、Ph 陽性急性淋巴性白血病（依文獻；香港許可證資料未載明適應症文字） |
| 預測新適應症 | 尤文氏肉瘤 (Ewing sarcoma) |
| TxGNN 預測分數 | 99.90% |
| 證據等級 | L3（原始資料標為 L2，但唯一的 Phase 2 試驗為單臂、非隨機，不符合 RCT 條件，故下調） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 20 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉 (MOA) 資料。從文獻可知，Dasatinib 是多標靶激酶抑制劑，作用對象包括 BCR-ABL、SRC 家族激酶、KIT 與 PDGFR。在 CML 中，其療效主要來自抑制 BCR-ABL。

尤文氏肉瘤是好發於青少年與年輕成人的骨與軟組織惡性腫瘤，轉移或復發後預後很差。前臨床研究顯示，SRC/FAK 訊號參與尤文氏肉瘤細胞的侵襲小體 (invadopodia) 形成、遷移與侵襲。Dasatinib 在肉瘤細胞株中也能抑制遷移與侵襲，並在依賴 SRC 的骨肉瘤細胞中誘導細胞凋亡。這是模型預測在機轉上的主要依據。

不過，這些證據幾乎都來自體外實驗。臨床上，一篇 2022 年的文獻回顧指出，dasatinib 單藥在包含尤文氏肉瘤與橫紋肌肉瘤的晚期肉瘤 Phase 2 試驗中未能奏效。因此機轉上說得通，但臨床上尚未證實。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00464620](https://clinicaltrials.gov/study/NCT00464620) | Phase 2 | 已完成 | 366 | Dasatinib 用於晚期肉瘤，評估反應率與 6 個月無惡化存活率。為單臂試驗，輸入資料未提供尤文氏肉瘤亞型的結果 |
| [NCT00788125](https://clinicaltrials.gov/study/NCT00788125) | Phase 1/2 | 已終止 | 7 | 兒童病患使用 dasatinib 合併 ifosfamide、carboplatin、etoposide。僅收 7 人即終止，幾乎無法評估療效 |
| [NCT06500819](https://clinicaltrials.gov/study/NCT06500819) | Phase 1 | 招募中 | 41 | B7-H3 CAR-T 細胞治療兒童與年輕成人的復發或難治實體瘤。**未使用 dasatinib**，不構成直接證據 |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [35655525](https://pubmed.ncbi.nlm.nih.gov/35655525/) | 2022 | Review | Sarcoma | 探討以 FAK-Src 複合體為標的治療 DSRCT、尤文氏肉瘤與橫紋肌肉瘤。指出 dasatinib 單藥在 Phase 2 試驗中對尤文氏肉瘤與橫紋肌肉瘤未達預期 |
| [26170970](https://pubmed.ncbi.nlm.nih.gov/26170970/) | 2015 | Review | Oncology Letters | 回顧 Src 在肉瘤中的角色，討論以 Src 作為藥物標的的可行性 |
| [35190971](https://pubmed.ncbi.nlm.nih.gov/35190971/) | 2022 | Review | Current Treatment Options in Oncology | 軟骨肉瘤的全身性治療回顧（間接相關，非針對尤文氏肉瘤） |
| [18202781](https://pubmed.ncbi.nlm.nih.gov/18202781/) | 2008 | 前臨床 | Oncology Reports | Dasatinib 在神經母細胞瘤與尤文氏肉瘤細胞株中具抗增殖與抗遷移活性 |
| [17363602](https://pubmed.ncbi.nlm.nih.gov/17363602/) | 2007 | 前臨床 | Cancer Research | Dasatinib 抑制多種肉瘤細胞株的遷移與侵襲，並在依賴 SRC 存活的骨肉瘤細胞中誘導凋亡 |
| [27566104](https://pubmed.ncbi.nlm.nih.gov/27566104/) | 2016 | 前臨床 | Neoplasia | 微環境壓力經由 Src 活化，促進尤文氏肉瘤的侵襲小體形成與細胞遷移 |
| [31521948](https://pubmed.ncbi.nlm.nih.gov/31521948/) | 2019 | 前臨床 | Neoplasia | Tenascin C 與 Src 協同促進尤文氏肉瘤的侵襲小體形成 |

---

## 香港上市資訊

香港共有 20 張 dasatinib 許可證，以下列出 5 張主要許可證。資料未提供核准適應症文字。

| 許可證號 | 品名 | 劑型 | 廠商 |
|---------|------|------|------|
| HK-55803 | SPRYCEL TAB 70MG | 錠劑 | BRISTOL-MYERS SQUIBB PHARMA (HK) LTD |
| HK-67775 | APO-DASATINIB TABLETS 20MG | 錠劑 | HIND WING CO LTD |
| HK-68522 | DASATINIB STADA TABLETS 50MG | 錠劑 | STADA PHARMACEUTICALS (ASIA) LIMITED |
| HK-66653 | DASATINIB SANDOZ TABLETS 20MG | 錠劑 | SANDOZ HONG KONG LIMITED |
| HK-68088 | DASATINIB SCIGEN TABLETS 70MG | 錠劑 | DCH AURIGA (HONG KONG) LIMITED - HEALTHCARE DIVISION |

---

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 標靶藥物（多標靶酪胺酸激酶抑制劑，TKI） |

其餘細胞毒性相關項目（骨髓抑制風險、致吐性、監測項目、處置防護）請參考原廠仿單的警語與注意事項。

---

## 安全性考量

- **文獻報告的不良反應**（來自 CML 病患的個案與病例系列）：胸水與乳糜胸、肺動脈高壓、心包積液、間質性肺炎，以及青少年病患的皮膚與軟組織感染。

其餘安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 尤文氏肉瘤的支持證據以體外研究為主。唯一的 Phase 2 肉瘤試驗為單臂設計，且文獻回顧指出 dasatinib 單藥在此亞型效果有限。
- 合併化療的 Phase 1/2 試驗僅收 7 人即終止。此外，香港產品安全性資料（仿單警語與禁忌）尚未取得，無法進入安全性篩選。

**若要推進需要：**
- 取得 NCT00464620 中尤文氏肉瘤亞群的療效數據。
- 從香港衛生署下載並解析仿單，補齊警語與禁忌症。
- 確認詳細的作用機轉資料 (MOA)。
- 評估合併療法（如搭配化療或其他 FAK/SRC 路徑藥物）的臨床前依據。

**補充：** 同一份預測清單中的第 2 名「骨髓性白血病」，實際上是 dasatinib 的既有適應症（已有 Phase 3 證據），並非真正的老藥新用發現。

> 本報告僅供研究參考，不構成醫療建議。老藥新用候選需經臨床驗證後才能應用。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

